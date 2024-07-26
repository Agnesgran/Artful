from django.contrib.auth.signals import user_logged_in
from allauth.account.signals import user_signed_up
from django.dispatch import receiver

@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    print(f'User {user.username} has logged in.')

@receiver(user_signed_up)
def user_signed_up_handler(sender, request, user, **kwargs):
    print(f'User {user.username} has signed up.')
