from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist


class Account(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    def __str__(self):
        return str(self.id)
        
class Message(models.Model):
    account = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL)
    content = models.CharField(max_length=255)
    def __str__(self):
        return self.content
    
class BugReport(models.Model):
    account = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255, null=True)
    prompt = models.TextField(null=True)
    messages = models.ManyToManyField(Message, related_name='bug_reports_messages', null=True, blank=True)
    most_correct = models.OneToOneField(Message, related_name='bug_report_most_correct', null=True, blank=True, on_delete=models.SET_NULL)
    date_created = models.DateField(auto_now=True)
    def __str__(self):
        return self.prompt
    
class Notification(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    
class Upvote(models.Model):
    accounts = models.ManyToManyField(Account, related_name="upvotes")
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)

#### methods ####

####MISC####
    
#needs to be redone post model change
#for graph
def getBugsSolvedPerMonth(accountObject):
    bugs_per_month = [0] * 12
    currentYear = datetime.now().year
    bug_reports = BugReport.objects.all()
    for bug_report in bug_reports:
        if bug_report.most_correct:
            if (bug_report.date_created.year == currentYear) and (bug_report.most_correct.account.user == accountObject.user):
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

def changePfp(user,picture):
    account = getAccountFor(user)
    account.profile_picture = picture
    account.save()

####notifications####

def getNotificationsFor(user):
    account = getAccountFor(user)
    notifications = Notification.objects.filter(account=account)
    return list(notifications)

####messages####

def makeMessage(message,account,report):
    message = Message(content=message,account=account)
    message.save()
    report.messages.add(message)
    report.save() 

def getMessageById(message_id):
    message = Message.objects.get(id=message_id)
    return(message)

####upvote####

def messageHasUpVote(message):
    try:
        upVote = Upvote.objects.get(message = message)
        return upVote
    except:
        print('Message has no upvote')
        return False


####bugReport####
    
def getReportById(report_id):
    report = BugReport.objects.get(id=report_id)
    return(report)

def getAllReports():
    return list(BugReport.objects.all())
    
def getUserBugReports(user):
    account = getAccountFor(user)
    reports = BugReport.objects.filter(account=account)
    return reports

def makeReport(user,prompt,title):
    account = getAccountFor(user)
    report = BugReport(title=title, prompt=prompt, account=account)
    report.save()

def makeBest(report,message):
    report.most_correct = message
    report.save()


####admin####

def adminDelete(type, num):
    try:
        index = int(num)#reindex
        if type == 'user':
            thing = User.objects.get(id=index)
        elif type == 'message':
            thing = Message.objects.get(id=index)
        elif type == 'bug_report':
            thing = BugReport.objects.get(id=index)
        elif type == 'account':
            thing = Account.objects.get(id=index)           
        else:
            print(f'Invalid type: {type}')
            return f'Invalid type: {type}'
        thing.delete()
        print(f'{type} Deleted.')
        return f'{type} Deleted.'
    except ObjectDoesNotExist:
        print(f'{type} not found with id {index}')
        return f'{type} not found with id {index}'
    except ValueError:
        print('Invalid number format')
        return 'Invalid number format'
    except Exception as e:
        print(f'An error occurred: {e}')
        return f'An error occurred: {e}'
