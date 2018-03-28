# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re

# Validations For Login
class UserManager(models.Manager):
	def validateUser(self, post_data):
		is_valid = True
		errors = []

		# Name and Username Validation
		if len(post_data.get('name')) and len(post_data.get('username')) < 3:
			is_valid = False
			errors.append('Your name is like my life and is to short!')
		# Email Validation
		if not re.search(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', post_data.get('email')):
			is_valid = False
			errors.append('You Crazy Bastard! You Must Enter A Valid Email!!!!')
		# Birthday Validation
		if len(post_data.get('birthdate')) == 0:
			is_valid = False
			errors.append('Im Unlike Your Parents... We Care About Your Birthdate... SO ENTER IT... NOW!')
		# Password Validation Of Less Than 8 Chars, And If Passwords Match
		if len(post_data.get('password')) < 8:
			is_valid = False
			errors.append('Your Password Must Be Like My Personality And Have 8 Characters!')
		if post_data.get('password_confirmation') != post_data.get('password'):
			is_valid = False
			errors.append('Your Password Is Like Me And My Ex... THEY DONT MATCH!')

		return (is_valid, errors)

# Data Base User Model
class User(models.Model):
	name = models.CharField(max_length = 100)
	username = models.CharField(max_length = 100)
	email = models.CharField(max_length = 100)
	password = models.CharField(max_length = 100)
	birthdate = models.DateField()
	favorites = models.ManyToManyField("Quote", related_name="favorites", default=None)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()

    # Show Formatted User Model
	def __str__(self):
		return "name:{}, username:{}, email:{}, password:{}, created_at:{}, updated_at:{}".format(self.name, self.username, self.email, self.password, self.created_at, self.updated_at)

# Validation For Quotes
class QuoteManager(models.Manager):
	def validateQuote(self, post_data):

		is_valid = True
		errors = []

		if len(post_data.get('content')) < 10:
			is_valid = False
			errors.append('Message must be more than 10 characters')
		return (is_valid, errors)

# Database Quotes Model
class Quote(models.Model):
	content = models.CharField(max_length = 255)
	author = models.CharField(max_length = 255)
	poster = models.ForeignKey(User, related_name = 'authored_quotes')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = QuoteManager()

	# Show Formatted Quotes Model
	def __str__(self):
		return 'content:{}, author:{}'.format(self.content, self.user)






