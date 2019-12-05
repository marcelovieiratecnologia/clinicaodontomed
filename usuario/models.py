from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.safestring import mark_safe
from django.conf import settings


# def user_avatar_path(instance, filename):
#     # return 'user_{0}/avatar/{1}'.format(instance.id, filename)
#     return 'avatar/user_{0}/{1}'.format(instance.id, filename)
#
# class CustomUsuarios(AbstractUser):
#     funcao_usuario = models.CharField(max_length=40, blank=True, null=True)
#     avatar = models.ImageField(upload_to=user_avatar_path)
#
#     def image_tag(self):
#         return mark_safe('<img src="/directory/%s" width="150" height="150" />' % (self.image))
#
#     image_tag.short_description = 'Image'
#
#
#     def __str__(self):
#         return self.username

FUNCAO = (
    ('RECEPICIONISTA',u'Recepicionista'),
    ('ATENDENTE',u'Atendente'),
    ('DENTISTA',u'Dentista'),
    ('MEDICO',u'Medico'),
    ('OUTROS',u'Outros')
)

def user_avatar_path(instance, filename):
    nomeimage = 'user_'+str(instance.id)+'.png'
    # return 'avatars/user_{0}/{1}'.format(instance.id, filename)
    return 'avatars/user_{0}/{1}'.format(instance.id, nomeimage)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    funcao = models.CharField(max_length=30, choices=FUNCAO,blank=True)
    image = models.ImageField(upload_to=user_avatar_path, null=True, blank=True)
    
    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_tag.short_description = 'Avatar'

    def __str__(self):
        return f'{self.user.username} Profile'

   
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()