from user import User
from myCustomException import MyCustomException, UserNotFoundError, UserAlreadyExistsError
class UserManager: 
    users = {}
    
    def __init__(self):
        self.users = {}
    
    def add_user(self, user: User):
        try:
            if user.username in self.users:
                raise UserAlreadyExistsError(f" Пользователь {user.username}  уже есть")
        except UserAlreadyExistsError as e:
            print(e) 
        else:
            self.users[user.username] = user
            print(f"Пользователь {user.username} добавлен  ")  
                
        
    def remove_user(self, username: str):
        try:
            if username in self.users:
                del self.users[username]
                print(f"Удален пользователь {username}")
            else:
                raise UserNotFoundError(f"Пользователь  {username} не найден")
        except UserNotFoundError as e:
            print(e) 
        
    def find_user(self, username: str):
        try:
            if username in self.users:
                print(f"Пользователь {username} найден ")
            else:
                raise UserNotFoundError(f"Пользователь {username} не найден")
        except UserNotFoundError as e:
            print(e) 
        finally:
            return self.users.get(username)
    
    def print_users(self):
        print("текущие пользователи")
        for key, value in self.users.items():
            print(f"имя: {key}, объкт: {value}")
        
        
        
        
        
   
        
    
    """	add_user(self, user: User): Добавляет пользователя в словарь. Если пользователь с таким именем уже существует, должен выбрасываться UserAlreadyExistsError.
	remove_user(self, username: str): Удаляет пользователя из словаря. Если пользователя с таким именем не существует, должен выбрасываться UserNotFoundError.
	find_user(self, username: str) -> User: Возвращает пользователя по имени. Если пользователя не существует, должен выбрасываться UserNotFoundError.
"""