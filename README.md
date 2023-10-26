# WAREAGLE-SQA2023-AUBURN
## COMP6710 Group Project. 
### Members: 
* Daniel Burris
* Nan Yang
* Krystal Lin

### Initial Stuff I've done:

1. Added pre-commit to .git/hooks with the following lines:
```
# Using the bandit tool to analyze all python files
# I want the verbose output so I know it's doing something
echo  "Running bandit security analysis on all python files"
python  -m  bandit  -v  -a  vuln  -r  -f  csv  -o  security_weaknesses  .
exit  0
```
2. Created fuzz.py with 5 functions that break 5 other functions. Not sure how detailed / advanced he wants us to get with these
```
if  __name__=='__main__':
	fuzzCheckIfWeirdYAML()
	fuzzScanForDefaultNamespace()
	fuzzScanForResourceLimits()
	fuzzGetYAMLFiles()
	fuzzGetValidTaints()
```
3. Added Github Action to fun fuzz.py following tutorial here: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python
```
# This workflow will install Python dependencies, run tests and lint with a single version of Python
# For more information see: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python  

name: Python application

on:
    push:
        branches: [ "main" ]
    pull_request:
        branches: [ "main" ]

permissions:
    contents: read

jobs:
    build:

        runs-on: ubuntu-

        steps:
        - uses: actions/checkout@v3
        - name: Set up Python 3.11
        uses: actions/setup-python@v3
        with:
            python-version: "3.11"
        - name: Install dependencies
        run: |
            python -m pip install --upgrade pip
            pip install ruamel.yaml
            pip install pandas
            pip install numpy
            pip install sarif_om
            pip install jschema_to_python
        - name: Run fuzz.py
        run: |
            python fuzz.py
```
