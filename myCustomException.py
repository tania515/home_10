class MyCustomException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
        
        
    def __str__(self):
        return self.message
    
    
class UserNotFoundError(MyCustomException):
    def __init__(self, message):
        super().__init__(message)
        
        
class UserAlreadyExistsError(MyCustomException):
    def __init__(self, message):
        super().__init__(message)
       