# fersat
## Arguments
```
usage: main.py [-h] input

positional arguments:
  input       Input expression

optional arguments:
  -h, --help  show this help message and exit
```

## Dependencies
The only libraries I'm using are **argparse** and **pycosat**.

## Input

You will just need to enter edge of the chess board length.

## Output

As the output you can have theese three options:

- *"Solution could not be determined within the propagation limit!"*.
- *"CNF is not satisfiable!"* - if there is no solution for entered edge length.
- If satisfiable then you will have an appropriate configuration of chess queens.
