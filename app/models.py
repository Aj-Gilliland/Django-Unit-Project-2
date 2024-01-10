from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    profile_picture = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.user

class Message(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    def __str__(self):
        return self.content

class BugReport(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    prompt = models.CharField(max_length=255, null=True)
    messages = models.ForeignKey(Message, related_name='bug_reports_messages', null=True, on_delete=models.SET_NULL)
    most_correct = models.OneToOneField(Message, related_name='bug_report_most_correct', null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.prompt

class Notification(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    def __str__(self):
        return self.content
    
class Upvote(models.Model):
    accounts = models.ManyToManyField(Account, related_name="upvotes")
    message = models.OneToOneField(Message, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)
    def __str__(self):
        return self.message

#### methods ####
    
#account 
      
#returns true if there is an account associated else returns false 
def hasAccount(user):
    try:
        account = Account.objects.get(user=user)   
        return True
    except:
        return False 

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

