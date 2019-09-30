# Sudoku
Sudoku solver in python!

This is a simple brute force sudoku solver, written in python.

The solver can be presented as a simple CLI or a TKinter based GUI.
## Difficulty levels
* Very Easy &#9745;
* Easy &#9745;
* Medium &#9745;
* Hard &#9745;
* Very Hard &#9745;

## Usage
To use the Sudoku solver as a CLI enter the following command from the root of the repository.
```bash
python3 sudoku.py
```
To use the Sudoku solver as a GUI enter the following command from the root of the repository. The program will solve the Sudoku board and display values as they are added in.
```bash
python3 sudoku.py -g
```
When running the program as a GUI you can enable fast solving using the `-f` flag. This will stop the program displaying the values as they are added in.
```bash
python3 sudoku.py -g -f
```

## Tests and Coverage
To run the unit tests with coverage enter the following command form the root of the repository.
```bash
pytest -v --cov sudoku
```