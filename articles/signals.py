from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
 
"""
@receiver(post_save, sender=Types)
def create_perm(sender, instance, created, **kwargs):
    if created:
        content_type = ContentType.objects.get_for_model(Types)
        Permission.objects.create(
            codename= 'editor_' +instance.slug,
            name='Can Edit '+instance.name,
            content_type=content_type,
        )

@receiver(post_delete, sender=Types)
def delete_perm(sender, instance, **kwargs):
    content_type = ContentType.objects.get_for_model(Types)
    permission = Permission.objects.filter(
        codename= 'editor_' +instance.slug,
        content_type=content_type,
    ) 
    #if permission is not None:
    permission.delete()
"""