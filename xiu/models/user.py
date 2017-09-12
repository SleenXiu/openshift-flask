from mongoengine import (
    Document, 
    StringField, 
    ObjectIdField,
)
from bson import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

class User(Document):
    id = ObjectIdField(primary_key=True, default=ObjectId)
    username = StringField()
    password = StringField()

    def save(self, *args, **kwargs):
        if self.password:
            self.password = generate_password_hash(self.password)
        return super(User, self).save(*args, **kwargs)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)