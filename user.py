class User:
    def __init__(self, username, address, age):
        self.__username = username
        self.__address = address
        self.__age = age
        
    def __str__(self):
        return f'Имя пользователя: {self.__username}, email: {self.__address}, Возраст: {self.__age}'
    
    @property
    def username(self):
        return self.__username