import sys
from models import *
from django.http import HttpResponse

def papersave(request):
	paper = Paper.objects.get(id=request.POST['paper'])
	paper.body = request.POST['body']
	paper.save()
	return HttpResponse("Success!")

def feedbacksave(request):
	paper = Paper.objects.get(id=request.POST['paper'])
	author = Author.objects.get(id=request.POST['author'])
	f = Feedback(content=request.POST['content'], paper=paper, author=author)
	f.save()
	notification = Notification(content=author.user.username+" submitted feedback on "+paper.question, author=paper.author)
	notification.save()
	return HttpResponse(f.id)

def delete(request):
	Feedback.objects.get(id=request.POST['id']).delete()
	return HttpResponse("Success!")