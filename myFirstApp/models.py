#from django.db import models
from mongoengine import Document,StringField,IntField,EmailField
  
class User(Document):  
    first_name = StringField(max_length=20)  
    last_name  = StringField(max_length=30)  
    contact    = IntField(default=0)  
    email      = EmailField(max_length=50)  
    age        = IntField(default=0)     
   
    def json(self):
        user_dict = {
            'first_name':self.first_name,
            'last_name':self.last_name,
            'contact':self.contact,
            'email':self.email,
            'age':self.age
        }
        return json.dumps(user_dict)
    
    meta = {
        'indexes':['first_name','last_name'],
        'ordering':['-date_created']
    }
   
       

 
    

   
