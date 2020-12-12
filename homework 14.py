#1

class User:
    def __init__(self, name):
        self.name = name
        
    def info(self):
        return ""    
    
    def describe(self):
        print(self.name,self.info())    
        
    def send_message(self, user, message):
        pass
    
    def post(self, message):
        pass
    
class Person(User):
    def __init__(self, name, birthday):
        super().__init__(name)
        self.birthday_date = birthday
        
    def subscribe(self, user):
        pass    
    
    def info(self):
        print("Date of birth:", self.birthday_date)
    
            
            
class Community(User):
    def __init__(self, name, description):
        super().__init__(name)
        self.description = description
        
    def info(self):
        print("Description:", self.description)
    
User("Vahan").describe()
Person(User,"July 13").info()
Community(User,"Some description text about user").info()