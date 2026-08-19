from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from django.core.mail import send_mail


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        # Logic to send a welcome email to the new user
        print(f"Welcome email sent to {instance.email}")
        subject = 'Welcome to Our Platform!'
        message = f'Hi {instance.username},\n\nThank you for registering at our platform. We are excited to have you on board!\n\nBest regards,\nThe Team'
        from_email = ''
        recipient_list = [instance.email]
        send_mail(subject, message, from_email, recipient_list)