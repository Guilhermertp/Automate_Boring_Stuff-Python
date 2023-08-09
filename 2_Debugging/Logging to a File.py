import logging

#to writ the error log to a file change the first line and put the paramater filename = 'name of log file.txt'
logging.basicConfig(filename = 'error_log.txt',level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

#logging.disable(logging.CRITICAL)#disables all the messages at he higher level and lower level that is the critical

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1,n+1): #now is corrected
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))
        
    logging.debug('Return value is %s' % (total))
    return total
print(factorial(5))

logging.debug('End of program')
