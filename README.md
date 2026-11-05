#calculator

a python 3 calculator used from the terminal, built step by step in sccm4910

##what will it do
Add, subtract, multiply and divide two numbers and display the result.

#how to run it
running tests: checks the right outputs.
- must include mutliply, subtract, divide and add
- source /opt/python-venv/sccm-4910/bin/activate
- run ./check.sh
- 5 results should all give "passed"
- exit status can be used to check if there were any failures: 0 = no failures 1 = failures found
=========================================================================================  
Run:
- python3 calculator.py or use ./run.sh
- enter the first number, operator(+-*/), then the second number
- the program prints the result: followed by the answer
- sample test: 5 * 5
- use ctrl + c to stop it form running
