from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(null=True, blank=True)

class Message(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)

class BugReport(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    prompt = models.CharField(max_length=255, null=True)
    messages = models.ForeignKey(Message, related_name='bug_reports_messages', null=True, on_delete=models.SET_NULL)
    most_correct = models.OneToOneField(Message, related_name='bug_report_most_correct', null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.content

class Notification(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    def __str__(self):
        return self.content
    
class Upvote(models.Model):
    accounts = models.ManyToManyField(Account)
    message = models.OneToOneField(Message, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)
    def __str__(self):
        return self.message

#### methods ####
    
#account   
def makeAccount(user):
    account = Account(user=user)     
    account.save()
    return account

def getAccountFor(user):
    account = Account.objects.get(user=user)
    return account     

#notifications
def getNotificationsFor(account):
    notifications = Notification.objects.filter(account=account)
    return notifications

