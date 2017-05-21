from django.db import models

class IdeaTag(models.Model):
    tag_text = models.CharField(max_length=10)

    def __str__(self):
        return self.tag_text
    pass

class Idea(models.Model):
    idea_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    votes = models.IntegerField(default=0)
    tags = models.ManyToManyField(IdeaTag)

    def __str__(self):
        return self.idea_text
