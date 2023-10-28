
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

4. Tried to build and run docker image from Dockerfile found in KubeSec.zip, but kept running into the following issues.
   ```
   cd C:\Users\Daniel\OneDrive - Auburn University\Documents\COMP6710\Project\WAREAGLE-SQA2023-AUBURN
   docker build -t docker_project .   
   ```

```
PS C:\Users\Daniel\OneDrive - Auburn University\Documents\COMP6710\Project\KubeSec\KubeSec-master> docker build .
[+] Building 405.3s (9/11)                                                                               docker:default
 => [internal] load build definition from Dockerfile                                                               0.1s
 => => transferring dockerfile: 545B                                                                               0.0s
 => [internal] load .dockerignore                                                                                  0.1s
 => => transferring context: 2B                                                                                    0.0s
 => [internal] load metadata for docker.io/continuumio/miniconda3:latest                                           0.6s
 => [1/7] FROM docker.io/continuumio/miniconda3@sha256:db9f536d96d49fe21b5f4ac3252781bb0d2a3b58dab2d8e44343b85014  0.0s
 => [internal] load build context                                                                                  0.1s
 => => transferring context: 91.64kB                                                                               0.0s
 => CACHED [2/7] WORKDIR /app                                                                                      0.0s
 => CACHED [3/7] RUN conda config --append channels conda-forge                                                    0.0s
 => CACHED [4/7] COPY environment.yml .                                                                            0.0s
 => ERROR [5/7] RUN conda env create -v -f environment.yml                                                       404.4s
------
 > [5/7] RUN conda env create -v -f environment.yml:
1.299 Collecting package metadata (repodata.json): ...working... done
316.5 Solving environment: ...working... done
392.5
392.5 CondaError: Downloaded bytes did not match Content-Length
392.5   url: https://repo.anaconda.com/pkgs/main/linux-64/mkl-2023.1.0-h213fc3f_46343.conda
392.5   target_path: /opt/conda/pkgs/mkl-2023.1.0-h213fc3f_46343.conda
392.5   Content-Length: 179885653
392.5   downloaded bytes: 109517169
392.5
392.5
------
Dockerfile:9
--------------------
   7 |     # Create the environment:
   8 |     COPY environment.yml .
   9 | >>> RUN conda env create -v -f environment.yml
  10 |
  11 |     # Make RUN commands use the new environment:
--------------------
ERROR: failed to solve: process "/bin/sh -c conda env create -v -f environment.yml" did not complete successfully: exit code: 1
PS C:\Users\Daniel\OneDrive - Auburn University\Documents\COMP6710\Project\KubeSec\KubeSec-master>
```
   
5. So I opened the docker image we had from Workshop2 to try and get this code to run and I kept running into the following issue. I will message Dr. Rahman about these issues I'm running into
```
   Traceback (most recent call last):
  File "/WAREAGLE-SQA2023-AUBURN/main.py", line 103, in <module>
    main('/WAREAGLE-SQA2023-AUBURN/TEST_ARTIFACTS')
  File "/WAREAGLE-SQA2023-AUBURN/main.py", line 68, in main
    content_as_ls, sarif_json   = scanner.runScanner( directory )
  File "/WAREAGLE-SQA2023-AUBURN/scanner.py", line 681, in runScanner
    rollingUpdateDict     = scanForRollingUpdates( yml_ )
  File "/WAREAGLE-SQA2023-AUBURN/scanner.py", line 487, in scanForRollingUpdates
    line_number = parser.show_line_for_paths(path_script,constants.SPEC_KW)
  File "/WAREAGLE-SQA2023-AUBURN/parser.py", line 349, in show_line_for_paths
    result = subprocess.check_output(["yq", yq_parameter , filepath], universal_newlines=True)
  File "/usr/lib/python3.10/subprocess.py", line 421, in check_output
    return run(*popenargs, stdout=PIPE, timeout=timeout, check=True,
  File "/usr/lib/python3.10/subprocess.py", line 503, in run
    with Popen(*popenargs, **kwargs) as process:
  File "/usr/lib/python3.10/subprocess.py", line 971, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "/usr/lib/python3.10/subprocess.py", line 1863, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: 'yq'
```
   
6. Anyway I went ahead and added myLogger.py from workshop 8 to the project and just put in a couple of logging functions in main.py. Haven't done much else with it yet. 
- (underneath if \_\_name\_\_ == '\_\_main\_\_':)
```    
    # Creating the logger object from myLogger.py
    simpleLogger  = myLogger.createLoggerObj()

    simpleLogger.info("Start of Log File")    
    main('/WAREAGLE-SQA2023-AUBURN/TEST_ARTIFACTS')
    
    simpleLogger.info("End of Log File")
```

- Underneath main() function: 
``` 
    # Simple logging statements just saying which directory this was run on and where the output file lives. 
    simpleLogger.info("Directory: ")
    simpleLogger.info(directory)
    simpleLogger.info("Output File: " + outfile)

    content_as_ls, sarif_json   = scanner.runScanner( directory )
    simpleLogger.info("Content as LS: " + content_as_ls)
    simpleLogger.info("SARIF JSON: " + sarif_json)
```
