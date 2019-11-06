from django.contrib.auth.models import User
from django.db import models


class Invitation(models.Model):
    from_user = models.ForeignKey(User,
                                  related_name="invitations_sent",
                                  on_delete=models.CASCADE)
    to_user = models.ForeignKey(User,
                                related_name="invitations_received",
                                verbose_name="user to Invite",
                                help_text="Please select a user you want to play a game with",
                                on_delete=models.CASCADE)
    message = models.CharField(max_length=300,
                               verbose_name="optional Message",
                               help_text="It's always nice to add a friendly message")
    timestamp = models.DateTimeField(auto_now_add=True)
