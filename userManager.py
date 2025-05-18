from user import User
class UserManager:
    users = {}
    
    def __init__(self):
        self.users = {}
    
    def add_user(self, user: User):
        self.users[user.username] = user  
                
        
    def remove_user(self, username: str):
        if username in self.users:
            del self.users[username]
        
    def find_user(self, username: str):
        return self.users.get(username)
    
    def print_users(self):
        for key, value in self.users.items():
            print(f"имя: {key}, объкт: {value}")
        
        
        
        
        
   
        
    
    """	add_user(self, user: User): Добавляет пользователя в словарь. Если пользователь с таким именем уже существует, должен выбрасываться UserAlreadyExistsError.
	remove_user(self, username: str): Удаляет пользователя из словаря. Если пользователя с таким именем не существует, должен выбрасываться UserNotFoundError.
	find_user(self, username: str) -> User: Возвращает пользователя по имени. Если пользователя не существует, должен выбрасываться UserNotFoundError.
"""