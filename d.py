from abc import ABC, abstractmethod
import logging

class LoggerInterface(ABC):
    @abstractmethod
    def enableConsoleLogging(self):
        raise NotImplemented

    @abstractmethod
    def enableLogToFile(self, filename):
        raise NotImplemented

    @abstractmethod
    def logDebug(self, message):
        raise NotImplemented
    
    @abstractmethod
    def logInfo(self, message):
        raise NotImplemented
    
    @abstractmethod
    def logWarning(self, message):
        raise NotImplemented
    
    @abstractmethod
    def logError(self, message):
        raise NotImplemented
    
    @abstractmethod
    def logCritical(self, message):
        raise NotImplemented

class LoggingLogger(LoggerInterface):

    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s: %(name)s [%(levelname)s]: %(message)s')
    
    def enableConsoleLogging(self):
        self.console_handler = logging.StreamHandler()
        self.console_handler.setFormatter(self.formatter)
        self.console_handler.setLevel(logging.DEBUG)
        self.logger.addHandler(self.console_handler)
    
    def enableLogToFile(self, filename):
        self.file_handler = logging.FileHandler(filename)
        self.file_handler.setFormatter(self.formatter)
    
    def logDebug(self, message):
        self.logger.debug(message)
    
    def logInfo(self, message):
        self.logger.info(message)
    
    def logWarning(self, message):
        self.logger.warning(message)
    
    def logError(self, message):
        self.logger.error(message)
    
    def logCritical(self, message):
        self.logger.critical(message)

def main():
    logger = LoggingLogger("foo")
    logger.enableConsoleLogging()
    logger.logDebug("Test message")

if __name__ == "__main__":
    main()