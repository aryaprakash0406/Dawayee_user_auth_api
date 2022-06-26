from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

#  Custom User Manager
class UserManager(BaseUserManager):
  def create_user(self, email, name, DOB,phone,Gender, password=None, password2=None):
      """
      Creates and saves a User with the given email, name, DOB and password.
      """
      if not email:
          raise ValueError('User must have an email address')

      user = self.model(
          email=self.normalize_email(email),
          name=name,
          DOB=DOB,
          phone=phone,
          Gender=Gender
      )

      user.set_password(password)
      user.save(using=self._db)
      return user

  def create_superuser(self, email, name,phone, DOB,Gender, password=None):
      """
      Creates and saves a superuser with the given email, name, tc and password.
      """
      user = self.create_user(
          email,
          password=password,
          name=name,
          DOB=DOB,
          phone=phone,
          Gender=Gender
      )
      user.is_admin = True
      user.save(using=self._db)
      return user

#  Custom User Model
class User(AbstractBaseUser):
  email = models.EmailField(
      verbose_name='Email',
      max_length=255,
      unique=True,
  )
  name = models.CharField(max_length=200,blank=True,null=True)
  Gender = models.CharField(max_length=200,blank=True,null=True)
  DOB = models.DateTimeField(blank=True,null=True)
  is_active = models.BooleanField(default=True)
  phone=models.IntegerField(unique=True,blank=True,null=True)
  is_admin = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
  updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

  objects = UserManager()

  USERNAME_FIELD = 'phone'
  REQUIRED_FIELDS = ['name', 'DOB','email','Gender']

  def __str__(self):
      return str(self.phone)

  def has_perm(self, perm, obj=None):
      "Does the user have a specific permission?"
      # Simplest possible answer: Yes, always
      return self.is_admin

  def has_module_perms(self, app_label):
      "Does the user have permissions to view the app `app_label`?"
      # Simplest possible answer: Yes, always
      return True

  @property
  def is_staff(self):
      "Is the user a member of staff?"
      # Simplest possible answer: All admins are staff
      return self.is_admin




