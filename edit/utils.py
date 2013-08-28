import sys
from models import *
from django.http import HttpResponse

def save(request, paper_id):
	paper = Paper.objects.get(id=paper_id)
	paper.body = request.POST['data']
	paper.save()
	return HttpResponse("Success!")

def feedbacksave(request, paper_id):
	paper = Paper.objects.get(id=paper_id)
	author = Author.objects.get(id=request.POST['author'])
	f = Feedback(content=request.POST['content'], paper=paper, author=author)
	f.save()
	notification = Notification(content=author.user.username+" submitted feedback on "+paper.question, author=paper.author)
	notification.save()
	return HttpResponse(f.id)

def delete(request):
	Feedback.objects.get(id=request.POST['id']).delete()
	return HttpResponse("Success!")