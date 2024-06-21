'''
Filename: d.py
Author: Ethan Lemieux
Purpose: Demonstrate the Dependency Inversion Principle (DIP)

'''

from abc import ABC, abstractmethod

class LoggingSystem(ABC):
    @abstractmethod
    def log(self):
        pass

class Logging(LoggingSystem):
    # Implementation of Logging
    ...

class Loguru(LoggingSystem):
    # Implementation of Loguru
    ...

class Google_auth(LoggingSystem):
    # Implementation of Google_auth
    ...

# class used for handling different authenticators

class LoggingAuthenticator:
    def __init__(self, logging_system: LoggingSystem):
        self.logging_system = logging_system

    def process_log(self, authenticator):
        self.logging_system.log(authenticator)
