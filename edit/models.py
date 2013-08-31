from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User)
    points = models.IntegerField(default = 5)
    def __unicode__(self):
		return self.user.username

class Paper(models.Model):
	#title = models.CharField(max_length=20)
	question = models.CharField(max_length=300)
	highlights = models.CharField(max_length=500, default='')
	body = models.TextField()
	pub_date = models.DateTimeField('pub_date')
	author = models.ForeignKey(Author)
	points = models.IntegerField()
	def __unicode__(self):
		return self.question

class Feedback(models.Model):
	content = models.TextField()
	author = models.ForeignKey(Author)
	paper = models.ForeignKey(Paper)
	chosen = models.BooleanField(default = False)

class Notification(models.Model):
	content = models.TextField()
	author = models.ForeignKey(Author)

class InviteCode(models.Model):
	code = models.CharField(max_length=6)
