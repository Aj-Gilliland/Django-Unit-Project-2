from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Account(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

class Message(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.CharField(max_length=255, unique=True)
 
class BugReport(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    prompt = models.CharField(max_length=255, null=True)
    messages = models.ForeignKey(Message, related_name='bug_reports_messages', null=True, on_delete=models.SET_NULL)
    most_correct = models.OneToOneField(Message, related_name='bug_report_most_correct', null=True, on_delete=models.SET_NULL)

class Notification(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    
class Upvote(models.Model):
    accounts = models.ManyToManyField(Account, related_name="upvotes")
    message = models.OneToOneField(Message, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)

#### methods ####

####MISC####
    
#needs to be redone post model change
#for graph
def getBugsSolvedPerMonth(accountObject):
    bugs_per_month = [0] * 12
    currentYear = datetime.now().year
    bug_reports = BugReport.objects.filter(messages__account=accountObject)
    print(bug_reports)
    for bug_report in bug_reports:
        print(bug_report.date_created)
        if bug_report.date_created.year == currentYear:
            month_index = bug_report.date_created.month - 1
            bugs_per_month[month_index] += 1
    print(bugs_per_month)
    return bugs_per_month
   
####account#### 
      
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

####notifications####

def getNotificationsFor(account):
    notifications = Notification.objects.filter(account=account)
    return notifications

####messages####

def makeMessage(content,account):
    message = Message(content=content,account=account)
    message.save()
    return message


####upvote####

def messageHasUpVote(message):
    try:
        upVote = Upvote.objects.get(message = message)
        return upVote
    except:
        print('Message has no upvote')
        return False

def addMessageToUpVote(account,message):
    ...

####bugReport####
    
def getUserBugReports(user):
    account = getAccountFor(user)
    reports = BugReport.objects.filter(account=account)
    return reports