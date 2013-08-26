import sys
from models import *
from django.http import HttpResponse

def save(request, paper_id):
	paper = Paper.objects.get(id=paper_id)
	paper.body = request.POST['data']
	f = Feedback(content=request.POST['content'], paper=paper, author=Author.objects.get(id=request.POST['author']))
	print f
	sys.stdout.flush()
	f.save()
	paper.save()
	return HttpResponse("success!")