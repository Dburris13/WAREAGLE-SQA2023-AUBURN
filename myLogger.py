import logging

# Got rid of the method so I could re-use logger in multiple files with from myLogger import myLogObj
fileName  = 'WAREAGLE_sqa2023_project.log' 
formatStr = '%(asctime)s %(message)s'
logging.basicConfig(format=formatStr, filename=fileName, level=logging.INFO)
myLogObj = logging.getLogger('sqa2023-logger') 
