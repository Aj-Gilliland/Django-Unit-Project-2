from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    profile_picture = models.ImageField(null=True, blank=True)

class Message(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

class BugReport(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    messages = models.ForeignKey(Message, null=True, on_delete=models.SET_NULL, related_name='bug_report_messages')
    most_correct = models.OneToOneField(Message, null=True, on_delete=models.SET_NULL, related_name='most_correct_bug_report')

class Notification(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

class Upvote(models.Model):
    accounts = models.ManyToManyField(Account, related_name="upvotes")
    message = models.OneToOneField(Message, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)
