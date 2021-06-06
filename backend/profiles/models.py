from django.db import models
from accounts.models import CustomUser 
from django.db.models.signals import post_save
from django.dispatch import receiver



def upload_to(instance, filename):
    return 'profiles/{filename}'.format(filename=filename)


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, related_name="profile", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
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

