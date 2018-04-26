class Singleton(type):
    def __init__(self, name, bases, mmbs):
        super(Singleton, self).__init__(name, bases, mmbs)
        self._instance = super(Singleton, self).__call__()

    def __call__(self, *args, **kw):
        return self._instance

'''
Write your own version of Filelog here!

The Filelog Class opens up a file and add log within. The
previous log, if any, should not be removed. Also, there
can be only one Filelog object at any time of this
program - that is, a second Filelog object will lead to
exact the same instance in the memory as the first one. 

At least three methods is required:
info(msg), warning(msg), and error(msg).
'''
class FileLog(metaclass = Singleton):
    def __init__(self, logger = None):
        import logging
        if logger == None:
            logger = logging.getLogger(__name__)
            logger.setLevel(logging.INFO)

            # create a file handler
            handler = logging.FileHandler('main.log')
            handler.setLevel(logging.INFO)

            # create a logging format
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)

            # add the handlers to the logger
            logger.addHandler(handler)
        self.logger = logger

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

'''
The following function serves as a simple test to check
whether the id of multiple instances of Filelog remain
the same.
'''

def FileLogTest(filelogInstance = None):
    if filelogInstance == None:
        raise ValueError('Filelog Instance doesn\'t exist')

    log = Logging()
    log.warning('One CS162 Filelog instance found with id ' + str(id(log)))
    log2 = Logging()
    log2.warning('Another CS162 Filelog instance Found with id ' + str(id(log2)))