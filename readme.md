# Sword Health DE Challenge

## Exercise 1

For the SQL exercise, I've included in the directory the necessary SQL scripts to create the table, fill it with data and the solution to retrieve the NPS score.


## Exercise 2

I've setup a Docker container to run Python the the word-count.py exercise. Add the input file to the shared_volume and just pass the filename as an argument to the function

#### Available Arguments
> --filename 'Name of file to process' [MANDATORY]
> --output_filename 'Name of the output file' [OPTIONAL, default = output.txt]
> --workers' 'Number of workers to use.' [OPTIONAL, default = 10]
> --chunk_size 'Number of rows to proccess per worker.' [OPTIONAL, default = $ { {filesize} \over workers} $]
> .

#### Running with local python instance

> python word-count.py --filename=input.txt

#### Running with provided docker solution

> cd python
> docker build -t py_word_counter .
> docker-compose run app --filename=input.txt



