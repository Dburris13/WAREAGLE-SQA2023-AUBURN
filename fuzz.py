from parser import checkIfWeirdYAML
from scanner import scanForDefaultNamespace
from scanner import scanForResourceLimits
from graphtaint import getYAMLFiles
from graphtaint import getValidTaints

# Just so I don't have to type the whole thing for each function
def formatException(eText):
    print(f"Exception Caught in function checkIfWeirdYAML from parser.py:\n\t EXCEPTION: {eText}")

# Fuzz the checkIfWeirdYAML from parser.py
# Easy to break because this function doesn't check for isInstance() first like so many of the other functions
def fuzzCheckIfWeirdYAML(): 
    try:
        checkIfWeirdYAML(123) # Passing an integer into a function that expects a string
    except Exception as e:
        formatException(e)

# Fuzz the scanForDefaultNamespace from scanner.py
# Easy to break because function doesn't check if file exists first
def fuzzScanForDefaultNamespace(): 
    try:
        scanForDefaultNamespace("┬─┬ノ( º _ ºノ)") # Passing a Naughty String value into a function that valid filename
    except Exception as e:
        formatException(e)

# Fuzz the scanForResourceLimits from scanner.py
# Break similarly to fuzzScanForDefaultNamespace
def fuzzScanForResourceLimits():
    try:
        scanForResourceLimits(456) # Passing an integer into a function that expects a string
    except Exception as e:
        formatException(e)      

# Fuzz the checkIfValidK8SYaml from graphtaint.py
# Easy to break because no type checking before plugging argument into os.walk()
def fuzzGetYAMLFiles(): 
    try:
        getYAMLFiles(123123) # Passing an integer into a function that expects a string
    except Exception as e:
        formatException(e)

# Fuzz the getValidTaints from graphtaint.py
# Just providing an invalid / unexpect lenght list object into the function
def fuzzGetValidTaints():
    inlist = [ "<script>alert(0)</script>"
"&lt;script&gt;alert(&#39;1&#39;);&lt;/script&gt;"
"<img src=x onerror=alert(2) />"
"<svg><script>123<1>alert(3)</script>"
"><script>alert(4)</script>" ]
    try:
        getValidTaints(inlist) # Passing a Naughty String value into a function that valid filename
    except Exception as e:
        formatException(e)


if __name__=='__main__':

    fuzzCheckIfWeirdYAML()
    fuzzScanForDefaultNamespace()
    fuzzScanForResourceLimits()
    fuzzGetYAMLFiles()
    fuzzGetValidTaints()