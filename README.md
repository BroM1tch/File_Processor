FileProcessor
=============

FileProcessor is a small and clean Python tool designed to read a text file, process its content, and write a structured report to an output file using modern and safe file-handling practices.

This project demonstrates proper usage of "with open", pathlib, clean project structure, and basic data processing logic. It is intended as a portfolio project to showcase solid Python fundamentals and good development habits.


Features
--------
- Reads text files from the input/ directory
- Cleans and processes each line
- Counts occurrences per line
- Writes a report to output/report.txt
- Uses pathlib for robust cross-platform paths
- Clean and readable code structure


Project Structure
-----------------
FileProcessor/
|
|-- src/
|   |-- fileprocessor.py
|
|-- input/
|   |-- sample.txt
|
|-- output/
|   |-- report.txt


How to Run
----------
From the project root, run:

python src/fileprocessor.py

After execution, a report will be generated in:

output/report.txt


Example
-------

Input (input/sample.txt):
-------------------------
apple
banana
apple
orange


Output (output/report.txt):
---------------------------
apple: 2
banana: 1
orange: 1


Technologies Used
-----------------
- Python 3
- pathlib
- Standard library only (no external dependencies)


Author
------
Michel Brochu
GitHub: https://github.com/BroM1tch


License
-------
MIT License
