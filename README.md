
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
3. Added Github Action to run fuzz.py by following tutorial here: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python
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

4. Created a docker image and modified main.py, scanner.py, and parser.py so that it will run to completion and I can test out the formatting of the logging functions.

I have hosted the docker build on docker hub under the URL 
```
docker pull mokraton/wareagle_project_sqa2023:latest
docker run --rm -it mokraton/wareagle_project_sqa2023:latest
cd WAREAGLE-SQA2023-AUBURN/
python3 main.py
```
The scripts take about 2-3 minutes to fully run, at the end you should see two new files (WAREAGLE-OUTPUT.csv and WAREAGLE_sqa2023_project.log)
    
5. Added logging functions to the following locations:
- Underneath **if \_\_name\_\_ == '\_\_main\_\_'**:
```    
    # Creating the logger object from myLogger.py
    simpleLogger  = myLogger.createLoggerObj()

    simpleLogger.info("Start of Log File")
    main('/WAREAGLE-SQA2023-AUBURN/TEST_ARTIFACTS/')
    
    simpleLogger.info("End of Log File")
```

- Underneath **main()** function: 
``` 
    # Simple logging statements just saying which directory this was run on and where the output file lives. 
    simpleLogger.info("Directory to be scanned: " + directory)
    simpleLogger.info("Results file located here: " + outfile)
    ....
    df_all          = pd.DataFrame( getCountFromAnalysis( content_as_ls ) )
    #outfile = Path(directory, "slikube_results.csv")
    simpleLogger.info("List of all YAML files parsed: " + df_all.to_string())
```
6. Added folder to store the Ansible/Puppet files for individual task to github and finished the invididual task. It seems pretty simple you just setup a docker image with all libraries needed to run vault4paper.py then spend an hour or so just walking through all the Ansible/Puppet files and replacing them with the outputs from vault4paper.py. Since it's individual I didn't push my results to this repo, but I did include quick MD document just detailing the steps I did to get it working.
