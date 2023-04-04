import logging
import os
import other_module

print('Current python dir:     ', os.path.dirname(__file__))

logging.basicConfig(format='%(levelname)s %(message)s [%(filename)s]',
                    filename=os.path.dirname(__file__)+'/my_logs.log',
                    encoding='utf-8',
                    level=logging.DEBUG,
                    filemode='w')

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')

other_module.fun()

print('Done.')
