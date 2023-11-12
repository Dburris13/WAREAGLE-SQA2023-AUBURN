import logging

def createLoggerObj(): 
    fileName  = 'WAREAGLE_sqa2023_project.log' 
    formatStr = '%(asctime)s %(message)s'
    logging.basicConfig(format=formatStr, filename=fileName, level=logging.INFO)
    myLogObj = logging.getLogger('sqa2023-logger') 
    return myLogObj
