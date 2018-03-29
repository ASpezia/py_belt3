# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
from datetime import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z09._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^[a-zA-Z0-9]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

#****copied from login_reg.  Adjust validations accordingly for exam**

# Create your models here.
class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors ={}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be more than 2 characters"
        if not NAME_REGEX.match(postData["first_name"]):
            errors["first_name_re"] = "User first name can only contain letters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be more than 2 characters"
        if not NAME_REGEX.match(postData["last_name"]):
            errors["last_name_re"] = "User last name can only contain letters"

        if len(postData['password']) < 8:
            errors["password"] = "Password must be greater than 8 characters"
        if not PASSWORD_REGEX.match(postData["password"]):
            errors["password_re"] = "password must contain only letter and numbers"
        if     postData['password'] != postData['conf_password']:
            errors['conf_password']= "password does not match"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email_re']= "Invalid email"

        return errors

    def login_validator(self, postData):
        errors ={}
        user = User.objects.get(email =postData['email'])
        if postData['email'] == user.email:
            password = user.password
            if not bcrypt.checkpw(postData['password'].encode(),password.encode()):
                errors['password'] = "Incorrect email/password"
        return errors


class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors ={}
        if len(postData['name']) < 3:
            errors["name"] = " name should be more than 3 characters"
        if not NAME_REGEX.match(postData["name"]):
            errors["first_name_re"] = "name can only contain letters"
        if len(postData['user_name']) < 3:
            errors["user_name"] = "User name should be more than 3 characters"
        if not NAME_REGEX.match(postData["user_name"]):
            errors["user_name_re"] = "User name can only contain letters"

        if len(postData['password']) < 8:
            errors["password"] = "Password must be greater than 8 characters"
        if not PASSWORD_REGEX.match(postData["password"]):
            errors["password_re"] = "password must contain only letters"
        if     postData['password'] != postData['conf_password']:
            errors['conf_password']= "password does not match"
        #if not EMAIL_REGEX.match(postData['email']):
        #    errors['email_re']= "Invalid email"

        return errors

    def login_validator(self, postData):
        errors ={}
        user_name = User.objects.get(name=postData['name'])
        if postData['user'] == user.user:
            password = user.password
            if not bcrypt.checkpw(postData['password'].encode(),password.encode()):
                errors['password'] = "Incorrect email/password"
        return errors

class User(models.Model):
    name = models.CharField(max_length =255)
    user_name = models.CharField(max_length =255)
    email =models.CharField(max_length =255)
    password = models.CharField(max_length =255)
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now_add =True)
    objects = UserManager()


class ItemManager(models.Manager):
    def item_validator(self, postData):
        errors = {}
        err = False

        if len(postData['item']) < 1:
            errors['item'] = "Item cannot be blank"
            err = True
        if len(postData['item ']) < 3:
            errorst['item'] = "itens description must be longer than 3 characters"
            err = True
class Item(models.Model):
    description = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now_add =True)
    wisher =  models.ForeignKey(User, related_name = 'wishes')
    item = models.ManyToManyField(User, related_name= 'items')
    objects = ItemManager()

    def __repr__(self):
        return "<item: {} {} {}>".format(self.destination, self.description, self.id)
