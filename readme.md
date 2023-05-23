# SH DE Challenge

## Exercise 1

For the SQL exercise, I've included in the directory the necessary SQL scripts to create the table, fill it with data and the solution ([code here](https://github.com/leonardo-melo/sh-de/blob/main/sql/solution.sql)) to retrieve the NPS score.

#### Runing with provided docker solution

```
> cd sql
> docker-compose up --build -d
> docker-compose run --rm db psql -h db -U postgres -d postgres -f solution.sql
> insert password: postgres
```
## Exercise 2

I've setup a Docker container to run Python the the word-count.py ([code](https://github.com/leonardo-melo/sh-de/blob/main/python/word-count.py)) exercise. To run it, just add your input file to the shared_volume directory and pass the filename as an argument to the function. The output will also be sent to the shared_volume. Optionally, there's additional arguments available for setup:

```
> --filename 'Name of file to process' [MANDATORY]
> --storage_dir 'Storage directory for input and output results' [OPTIONAL, default = shared_volume]
> --output_filename 'Name of the output file' [OPTIONAL, default = output.txt]
> --chunk_size 'Number of rows to proccess per worker.' [OPTIONAL, default = $ { {filesize} \over workers} $]
> --workers' 'Number of workers to use.' [OPTIONAL, default = 10]
```

#### Running with local python instance

```
> cd python
> python word-count.py --filename=input.txt
```

#### Running with provided docker solution

```
> cd python
> docker build -t py_word_counter .
> docker-compose run app --filename=input.txt
```



