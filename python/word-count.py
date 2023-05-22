import concurrent.futures
import argparse
import time
import os

def read_file_chunk(filename, start, end):
    with open(filename, 'r') as file:
        file.seek(start)
        chunk = file.readlines(end - start)
        return chunk

def count_words(chunk):
    word_count = {}
    for line in chunk:
        words = line.strip().split()
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count

def write_word_count(filename, word_count):
    with open(filename, 'w') as file:
        for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
            file.write(f"{word} {count}\n")

def main(params):
    input_file = "shared_volume/" + params.filename
    output_file = "shared_volume/" + params.output_filename
    max_workers = int(params.workers)
    start_time = time.time()

    file_size = os.path.getsize(input_file)
    chunk_size = file_size // max_workers
    if(params.chunk_size is not None):
        chunk_size = int(params.chunk_size)


    with open(input_file, 'r') as file:
        lines = file.readlines()

    chunks = [lines[i:i+chunk_size] for i in range(0, len(lines), chunk_size)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for chunk in chunks:
            future = executor.submit(count_words, chunk)
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
    parser.add_argument('--output_filename', required=False, help='Name of the output file.', default="output.txt")
    parser.add_argument('--workers', required=False, help='Number of workers to use.', default=10)
    parser.add_argument('--chunk_size', required=False, help='Number of rows to proccess per worker.')

    args = parser.parse_args()

    main(args)
