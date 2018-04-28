from products.models import Product

from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):

    def create_user(self ,  email, user_name , password=None ,is_normal=True , is_instructor = False , is_staff= False , is_admin=False):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        if not password:
            raise ValueError('Users must have a password')

        if not user_name:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            user_name = user_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_instructoruser(self, email,user_name, password=None):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            user_name,
            password=password,
        )
        user.instructor = True
        user.save(using=self._db)
        return user

    def create_normaluser(self, email,user_name, password=None):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            user_name,
            password=password,
        )
        user.normal = True
        user.instructor= True
        user.save(using=self._db)
        return user



    def create_staffuser(self, email,user_name, password=None):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
        email,
        user_name,
        password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, user_name,password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            user_name,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    objects = UserManager()
    joinedCourses = models.ManyToManyField(Product, null=True ,blank=True)
    instrCourse = models.OneToOneField(Product , null=True , blank=True ,related_name="instructor", on_delete=models.CASCADE)

    email = models.EmailField(verbose_name='email',max_length=255,unique=True,)
    user_name = models.CharField(max_length= 255 ,blank=True,null=False )
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    # notice the absence of a "Password field", that's built in.
    normal = models.BooleanField(default=True)
    instructor = models.BooleanField(default=True)


    USERNAME_FIELD = 'email'
    # EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name'] # Email & Password are required by default.

    #def get_username(self):
        # The user is identified by their email address
      #  return self.user_name

    def get_email(self):
        # The user is identified by their email address
        return self.email

    # def get_short_name(self):
    #     # The user is identified by their email address
    #     return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_instructor(self):
        "Is the user a member of staff?"
        return self.instructor
    @property
    def is_normal(self):
        "Is the user a member of staff?"
        return self.normal

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active
