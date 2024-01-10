from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
<<<<<<< HEAD
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
=======
    user = models.OneToOneField(User, on_delete=models.CASCADE)
>>>>>>> 8f6b4468ecf7fe696f51baebea33fb0062c6c183
    profile_picture = models.ImageField(null=True, blank=True)

class Message(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

class BugReport(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
<<<<<<< HEAD
    messages = models.ForeignKey(Message, null=True, on_delete=models.SET_NULL, related_name='bug_report_messages')
    most_correct = models.OneToOneField(Message, null=True, on_delete=models.SET_NULL, related_name='most_correct_bug_report')
=======
    messages = models.ForeignKey(Message, related_name='bug_reports_messages', null=True, on_delete=models.SET_NULL)
    most_correct = models.OneToOneField(Message, related_name='bug_report_most_correct', null=True, on_delete=models.SET_NULL)
>>>>>>> 8f6b4468ecf7fe696f51baebea33fb0062c6c183

class Notification(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

class Upvote(models.Model):
<<<<<<< HEAD
    accounts = models.ManyToManyField(Account, related_name="upvotes")
    message = models.OneToOneField(Message, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)
=======
    accounts = models.ManyToManyField(Account)
    message = models.OneToOneField(Message, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)

>>>>>>> 8f6b4468ecf7fe696f51baebea33fb0062c6c183
