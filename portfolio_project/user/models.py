from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
	def create_user(self, username, password, name, email, phone):
		user = self.model(
			username=username,
			name=name,
			email=self.normalize_email(email),
			phone=phone,
			date_joined=timezone.now(),
			is_superuser=0,
			is_staff=0,
			is_active=1
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, username, name, email, phone, password):
		user = self.create_user(
			username=username,
			password=password,
			name=name,
			email=email,
			phone=phone,
		)
		user.is_superuser=1
		user.is_staff=1
		user.save(using=self._db)
		return user
	
class User(AbstractBaseUser):
	username = models.CharField(unique=True, max_length=128)
	password = models.CharField(max_length=128)
	name = models.CharField(max_length=128)
	phone = models.CharField(max_length=32)
	email = models.CharField(max_length=254)
	date_joined = models.DateTimeField()
	last_login = models.DateTimeField(blank=True, null=True)
	is_superuser = models.IntegerField()
	is_staff = models.IntegerField(blank=True, null=True)
	is_active = models.IntegerField(blank=True, null=True)

	objects = UserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['name', 'phone', 'email']

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	class Meta:
		db_table = 'user'
