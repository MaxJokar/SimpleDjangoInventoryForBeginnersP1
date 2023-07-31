from django.db import models
from django.contrib.auth.models import  BaseUserManager, AbstractBaseUser

# 1.Customizing Admin Panel in Django :

# 3. The CustomUser Manger : to  create both  USER or Admin for  Admin Panel:
class CustomUserManger(BaseUserManager):
    def create_user(self, email,name,family, mobile_number,gender=True, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password,name,family,etc.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not mobile_number :
            raise ValueError('Users must have an mobile_number')

        user = self.model(
            #normalize: corrects erros or mistakes Users type:
            email=self.normalize_email(email),
            name = name,
            family = family,
            mobile_number = mobile_number,
            gender = gender,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name,family,mobile_number, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password,etc.
        """
        user = self.create_user(
            email,
            password=password,
            name = name,
            family = family,
            mobile_number = mobile_number,
            )
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user



#2.To create my model User Based on email  :
class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True,)
    name= models.CharField(max_length=50)
    family=models.CharField(max_length=50)
    mobile_number=models.CharField(max_length=11 , unique=True)
    gender=models.BooleanField(default=True, blank=True,null=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=True)

    # To enter the Customized Admin Panel
    USERNAME_FIELD = 'email'
    # Required filds for  createsuperuser
    REQUIRED_FIELDS = ['name','family','mobile_number']
    # The manager ofr CustomUser which is  set to objects: give up there here
    objects = CustomUserManger()


    #  Below Function are  the default  Proposal based on Djnago customized Admin Panel in Django Documentation :
    # __str__ appearS on the website face After  USER  login <welcome ..copy().Max Jokar....>
    def __str__(self):  # sourcery skip: use-fstring-for-concatenation
        return self.name+"  "+self.family

    def has_perm(self, perm, obj=None):
        # Does the user have a specific permission?
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # Does the user have permissions to view the app `app_label`?
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        # Is the user a member of staff?
        # Simplest possible answer: All admins are staff
        return self.is_admin



