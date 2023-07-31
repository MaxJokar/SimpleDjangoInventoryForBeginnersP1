from django.db import models
from django.utils import timezone
# from account.models import User
from django.contrib.auth.models import User

# install crispy library helps to have text and images from 2 tables in one together
#pip install django-crispy-form: setting add INSTALLED_APPS:crispy_forms


# 1.Define our Memoir model:
class Memoir(models.Model):
    memoir_title = models.CharField(max_length=200, verbose_name='memoir title ')
    Memoir_text = models.TextField(verbose_name='memoir text ')
    register_data = models.DateTimeField(default=timezone.now)
    # the memoir is False first.Admin can True it to be visible .If it's not True don't show it .
    is_active = models.BooleanField(default=False)
    # null-True :means even the users without registeration can leave their memor
    user_registered = models.ForeignKey(User, on_delete = models.CASCADE,null=True)

    # returns a string (shows ) that is exactly rendered as the display name of instances for that model.
    def __str__(self): # in Terminal , Admin panel, shell ,
        return self.memoir_title





# 2.Define our Galley (images) Memoir model:
# for related_name , we should define a funcation to control in which the pic must be uploaded!
# instance of the memoirGallery
def upload_gallery_image(instance , filename):
    # return f"images/memoir/gallery/{filename}" works properly ! you can see the folder gallery created .
    # using instance we can  change our address following:
    return f"images/memoir/{instance.memoir.memoir_title}/gallery/{filename}"

class MemoirGallery(models.Model):

    Memoir_image_name = models.ImageField(upload_to=upload_gallery_image,verbose_name='memoir image ')
    #related_name = images  ,also added to Memoir as its field: Unknown field(s) (Memoir_image_name) specified for MemoirGallery
    # memoir code :using it we can connect this class to the Memoir !very CRUICIAL !!!
    # related :relation between one to N in  occurs in child
    # memoir code
    memoir=models.ForeignKey(Memoir, on_delete=models.CASCADE,null=True, related_name='images')





# To like a  Memoir we make  the following Model:
class MemoirLike(models.Model):
    # user liker code
    user_liked = models.ForeignKey(User,  on_delete = models.CASCADE,null=True)
    # memoir liked code
    memoir = models.ForeignKey(Memoir, on_delete=models.CASCADE,null=True)




# Admin can block a  User , could be from db or via Syntax
class UserBlocked(models.Model): # BlockedUSer
    # Using more than one foriegnKey use relatedname to avoid interference!
    user_blcoker =  models.ForeignKey(User, on_delete = models.CASCADE,null=True,related_name="blocker")
    user_blocked  = models.ForeignKey(User, on_delete = models.CASCADE,null=True,related_name="blocked")
    register_data = models.DateTimeField(default=timezone.now)
