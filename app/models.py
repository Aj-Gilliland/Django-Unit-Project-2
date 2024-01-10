from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(null=True, blank=True)

class Message(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

class BugReport(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    messages = models.ForeignKey(Message, related_name='bug_reports_messages', null=True, on_delete=models.SET_NULL)
    most_correct = models.OneToOneField(Message, related_name='bug_report_most_correct', null=True, on_delete=models.SET_NULL)

class Notification(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

class Upvote(models.Model):
    accounts = models.ManyToManyField(Account)
    message = models.OneToOneField(Message, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)

