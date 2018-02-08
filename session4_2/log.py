class Singleton(type):
    def __init__(self, name, bases, mmbs):
        super(Singleton, self).__init__(name, bases, mmbs)
        self._instance = super(Singleton, self).__call__()

    def __call__(self, *args, **kw):
        return self._instance

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

# log = Logging()
# log.warning('Multiple Instances of CS162 Found')
# log2 = Logging()
# print(id(log), id(log2))
# log2.warning('Multiple Instances of log Found')