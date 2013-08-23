from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from edit.models import *

def index(request):
	latest_paper_list = Paper.objects.order_by('-pub_date')[:5]
	template = loader.get_template('edit/index.html')
	context = RequestContext(request, {
		'latest_paper_list': latest_paper_list,
		'user': request.user,
	})
	return HttpResponse(template.render(context))

def edit(request, paper_id):
	print paper_id
	paper = Paper.objects.get(id=paper_id)
	feedback_list = Feedback.objects.filter(paper=paper)
	print feedback_list
	template = loader.get_template('edit/paper.html')
	context = RequestContext(request, {
		'paper': paper,
		'feedback_list': feedback_list,
	})

	return HttpResponse(template.render(context))

def login(request):
	return render_to_response('edit/login.html',{},context_instance=RequestContext(request))

def signup(request):
	return render_to_response('edit/signup.html',{},context_instance=RequestContext(request))

def createuser(request):
	if request.POST['pass'] != request.POST['confirm']:
		return HttpResponse("Your passwords don't match, go back and try again")
	else:
		user = User.objects.create_user(request.POST['username'], '', request.POST['pass'])
		author = Author(user = user, points=5)
		author.save()
		return HttpResponse("Success!")

@login_required
def submitfeedback(request):
	paper = Paper.objects.all().get(id=request.POST['paper'])
	feedback = Feedback(content=request.POST['feedback'], author=Author.objects.all().get(user=request.user), paper=paper)
	feedback.save()
	return HttpResponse("Success!")

@login_required
def submit(request):
	return render_to_response('edit/submit.html',{},context_instance=RequestContext(request))

@login_required
def submitpaper(request):
	print request.POST['question']
	print request.POST['body']
	paper = Paper(question = request.POST['question'], body = request.POST['body'], author=Author.objects.all().get(user=request.user), pub_date = timezone.now())
	paper.save()
	print paper.id
	return HttpResponse("Thanks brah!")