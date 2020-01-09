from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    pass


class Link(models.Model):
    class Status(models.IntegerChoices):
        FRIENDS = 1
        BLOCKED = 2

    to_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='friends')

    from_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)

    status = models.IntegerField(choices=Status.choices)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('to_user', 'from_user')
        verbose_name = "Link"
        verbose_name_plural = "Links"

    def __str__(self):
        return self.from_user

    def save(self, *args, **kwargs):
        if self.to_user == self.from_user:
            raise Exception(
                'attempted to create a self link situation.')
        super(Link, self).save(*args, **kwargs)


class Invitation(models.Model):
    to_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='received_invitations')

    from_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sent_invitations')

    body = models.TextField(max_length=255, blank=True, default='')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('to_user', 'from_user')
        verbose_name = "Invitation"
        verbose_name_plural = "Invitations"

    def __str__(self):
        return self.from_user

    def save(self, *args, **kwargs):
        if self.to_user == self.from_user:
            raise Exception('attempted to create a self invitation situation.')
        super(Invitation, self).save(*args, **kwargs)
