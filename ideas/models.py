from django.db import models

class Idea(models.Model):
    idea_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.idea_text

