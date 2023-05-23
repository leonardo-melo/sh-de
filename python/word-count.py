import concurrent.futures
import argparse
import time
import os
import re

def clean_word(word: str) -> str:
    """
    Cleans a word by removing non-word characters and converting it to lowercase.

    Args:
        word: The word to clean.

    Returns:
        The cleaned word.
    """
    pattern = r"[^\w]" 
    word = word.lower()
    cleaned_word = re.sub(pattern, "", word)
    return cleaned_word

def calculate_chunk_size(params:argparse.Namespace, file_size: int, max_workers:int) -> int:
    """
    Calculates the chunk size for dividing the file into chunks to process.

    Args:
        arguments: The parsed command-line arguments.
        file_size: The size of the input file in bytes.
        max_workers: The maximum number of workers to use.

    Returns:
        The calculated chunk size.
    """
    chunk_size = file_size // max_workers
    if params.chunk_size is not None:
        chunk_size = int(params.chunk_size)
    return chunk_size

def read_file_chunk(filename: str, start:int, end:int) -> list[str]:
    """
    Reads a chunk of lines from a file.

    Args:
        filename: The name of the file to read.
        start: The starting position in the file.
        end: The ending position in the file.

    Returns:
        The lines read from the file as a list of strings.
    """
    with open(filename, 'r') as file:
        file.seek(start)
        chunk = file.readlines(end - start)
        return chunk

def count_words(chunk: list[str]) -> dict:
    """
    Counts the occurrences of words in a chunk of lines.

    Args:
        chunk: The chunk of lines to process.

    Returns:
        A dictionary containing the word count.
    """
    word_count = {}
    for line in chunk:
        words = line.strip().split()
        for word in words:
            word = clean_word(word)
            word_count[word] = word_count.get(word, 0) + 1
    return word_count

def write_word_count(filename:str, word_count: dict):
    """
    Writes the word count dictionary to a file.

    Args:
        output_filename: The name of the output file.
        word_count: The word count dictionary.
    """
    with open(filename, 'w') as file:
        for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
            file.write(f"{word} {count}\n")

def main(params: argparse.Namespace):
    start_time  = time.time()
    input_file  = f'{params.storage_dir}/{params.filename}'
    output_file = f'{params.storage_dir}/{params.output_filename}'
    max_workers = int(params.workers)    
    file_size   = os.path.getsize(input_file)
    chunk_size  = calculate_chunk_size(params, file_size, max_workers)
    num_chunks  = file_size // chunk_size

    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:

        futures = []
        for i in range(num_chunks):
            start = i * chunk_size
            end = start + chunk_size if i < num_chunks - 1 else file_size
                
            chunk = executor.submit(read_file_chunk, input_file, start, end)

            future = executor.submit(count_words, chunk.result())
            futures.append(future)

        word_count = {}
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            for word, count in result.items():
                word_count[word] = word_count.get(word, 0) + count

        executor.submit(write_word_count, output_file, word_count)

    end_time = time.time()
    print(f'Word count complete, took {end_time-start_time} seconds and stored in {output_file}.')

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Count words from received file')

    parser.add_argument('--filename', required=True, help='Name of file to process.')
    parser.add_argument('--storage_dir', required=False, help='Storage directory name.', default="shared_volume")
    parser.add_argument('--output_filename', required=False, help='Name of the output file.', default="output.txt")
    parser.add_argument('--workers', required=False, help='Number of workers to use.', default=10)
    parser.add_argument('--chunk_size', required=False, help='Number of rows to proccess per worker.')

    args = parser.parse_args()

    main(args)
