class user:
    
    _active_user=0
    
    @classmethod
    def init_user(cls,data_str):
        name,acc_money=data_str.split(",")
        return cls(name,acc_money)
    
    @classmethod
    def active_user(cls):
        return f"there are currently {cls._active_user} active user."
    
    def __init__(self,name,acc_money):
        self.name=name
        self.acc_money=acc_money
        user._active_user+=1
            
    def balance(self):
        return f"Balance left is ${self.acc_money}"
    
    def username(self):
        return f"Username is {self.name}"
    
    def logout(self):
        user._active_user-=1
        return f"{self.name} is logged out."
        
