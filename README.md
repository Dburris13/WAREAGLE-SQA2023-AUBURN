# WAREAGLE-SQA2023-AUBURN
COMP6710 Group Project. 
Members: 
* Daniel Burris
* Nan Yang
* Krystal Lin


4a.
    Added pre-commit to .git/hooks
        Added the following lines: 
        # Using the bandit tool to analyze all python files
        # I want the verbose output so I know it's doing something
        echo "Running bandit security analysis on all python files"
        python -m bandit -v -a vuln -r -f csv -o security_weaknesses .
        exit 0
4b. 
    Created fuzz.py with 5 functions that break 5 other functions. Not sure how detailed / advanced he wants us to get with these
    Added Github Action to fun fuzz.py following tutorial here: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python


