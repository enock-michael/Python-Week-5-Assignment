class Device:
    def _init_(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"

class Smartphone(Device):
    def _init_(self, brand, model, storage, battery, os):
         constructor
        super()._init_(brand, model)
        self.storage = storage
        self.battery = battery
        self.os = os
    
    def make_call(self, number):
        return f" Calling {number} using {self.device_info()}..."
    
    def check_battery(self):
        return f" Battery level: {self.battery}%"
    
    def install_app(self, app_name):
        return f" Installing {app_name} on {self.device_info()} running {self.os}."


 (Polymorphism Example)
class SuperSmartphone(Smartphone):
    def _init_(self, brand, model, storage, battery, os, ai_chip):
        super()._init_(brand, model, storage, battery, os)
        self.ai_chip = ai_chip
    
   method (Polymorphism)
    def make_call(self, number):
        return f"AI-powered call to {number} using {self.device_info()} with {self.ai_chip}!"
