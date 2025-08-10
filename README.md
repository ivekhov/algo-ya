
Usage


Create new task folder from copy-paste ./algokraken/task_template
Fill input , output, expected files according to task
Code ...
in main() leave only needed pairs of files .txt

Sc #1 - if only from test: 

Edit in test.py 
- TASK_NAME
- check SPRINT_NAME is correct
- list of files with examples

```bash

uv build && uv sync


```

From algo-ya start
```bash
uv run pytest algokraken/sprint_name/task_name/test.py
```


Sc #2 - just script
From pwd start

```bash
uv run python solution.py
```







```bash

# cd to dir with  solution.py
$ uv run python3 solution.py


#$ more output.txt

```

Building project:

```bash
$ uv build


```



For Makefile:

lint:
	uv run ruff check algokraken

test:
	uv run pytest -vv

build:
	uv build

	 
Style-guide:

```bash
# all project
$ uv run ruff check algokraken

# if inside directory
$ uv run ruff check .
```

Testing:








---

