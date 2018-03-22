# encoding=utf8
from django.db import models
from django.core.validators import URLValidator


class New(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    date = models.DateField()
    url = models.TextField(validators=[URLValidator()])
    media = models.ImageField()

    def __str__(self):
        return "{0} ({1})".format(self.title, self.date)


class Challenge(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Idea(models.Model):
    title = models.CharField(max_length=128, blank=True, default="")
    challenge = models.ForeignKey(Challenge, related_name="idea_challenge", null=True, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()
    public = models.BooleanField()
    email = models.EmailField(null=True)

    def __str__(self):
        idea_str = "Idea by {0}".format(self.email)
        if self.title and self.challenge:
            idea_str += " ({0})".format(self.challenge)
        idea_str += " at {0}".format(self.date)
        return idea_str
