from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Bugs(models.Model):
    ToDo = 'To Do'
    Doing = 'Doing'
    Done = 'Done'
    STATUS_CHOICES = ((ToDo, 'To Do'),
                      (Doing, 'Doing'), (Done, 'Done'))

    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=False)
    username = models.ForeignKey(User, default=None)
    created_date = models.DateTimeField(blank=True, default=None, null=True)
    waiting_date = models.DateTimeField(blank=True, default=None, null=True)
    in_progress_date = models.DateTimeField(
        blank=True, default=None, null=True)
    completion_date = models.DateTimeField(blank=True, default=None, null=True)
    views = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    status = models.CharField(
        max_length=40, choices=STATUS_CHOICES, default=ToDo)
      

    def __str__(self):
        return self.name
        
class UpvoteBug(models.Model):
    upvoted_bug = models.ForeignKey(Bugs, default=None)
    user = models.ForeignKey(User, default=None)

    def __str__(self):
        return str(self.user)


class BugComments(models.Model):
    bug_ticket = models.ForeignKey(Bugs, null=True)
    username = models.ForeignKey(User, null=None)
    comment = models.TextField(blank=False)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.comment

    
    
    