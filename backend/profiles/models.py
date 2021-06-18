from django.db import models
from accounts.models import CustomUser 
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField


def upload_to(instance, filename):
    return 'profiles/{filename}'.format(filename=filename)


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, related_name="profile", on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    mobile = PhoneNumberField( max_length=125, unique=True, blank=True, null=True,
                              help_text='Contact phone number')  
    
    age = models.IntegerField(null= True, blank=True)
    job= models.CharField( max_length=150,null= True, blank=True)
    country = models.CharField( max_length=150,null= True, blank=True)
    about = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField( upload_to = upload_to,default = 'def.png')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.user_name

    class Meta:
        ordering = ("created_at",)

@receiver(post_save, sender=CustomUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()