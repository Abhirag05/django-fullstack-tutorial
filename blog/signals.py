from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import Blog

@receiver(pre_save, sender=Blog)
def blog_pre_save(sender, instance, **kwargs):
    print(f"Blog post is about to be saved: {instance.title}")

@receiver(post_save, sender=Blog)
def blog_post_save(sender, instance, created, **kwargs):
    if created:
        print(f"New blog post created: {instance.title}")
    else:
        print(f"Blog post updated: {instance.title}")