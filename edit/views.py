from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login


import sys

from edit.models import *

@login_required
def index(request):
	latest_paper_list = Paper.objects.all()
	latest_paper_list = latest_paper_list.filter(points__gte=1)
	latest_paper_list = latest_paper_list.order_by('-points', '-pub_date')[:20]
	template = loader.get_template('edit/index.html')
	author = Author.objects.all().get(user=request.user)
	notifications = Notification.objects.filter(author=author)

	context = RequestContext(request, {
		'latest_paper_list': latest_paper_list,
		'notification_list': notifications,
		'user': request.user,
		'author': author,
	})

	for n in notifications:
		n.delete()

	return HttpResponse(template.render(context))

def signout(request):
	logout(request)
	return HttpResponseRedirect("/")

@login_required
def edit(request, paper_id):
	print paper_id
	paper = Paper.objects.get(id=paper_id)
	feedback_list = Feedback.objects.filter(paper=paper)
	print feedback_list
	template = loader.get_template('edit/paper.html')

	ownPaper = Author.objects.all().get(user=request.user) == paper.author
	author = Author.objects.get(user=request.user)
	context = RequestContext(request, {
		'username': request.user.username,
		'author': author,
		'paper': paper,
		'feedback_list': feedback_list,
		'ownPaper': ownPaper
	})

	return HttpResponse(template.render(context))

# def signin(request):
# 	return render_to_response('edit/login.html',{},context_instance=RequestContext(request))

def signup(request):
	return render_to_response('edit/signup.html',{},context_instance=RequestContext(request))

def createuser(request):
	if request.POST['pass'] != request.POST['confirm']:
		return HttpResponse("Your passwords don't match, go back and try again")
	else:
		if User.objects.filter(username = request.POST['username']).count()>0:
			return HttpResponse("Your username is not unique! Try another one")

		user = User.objects.create_user(request.POST['username'], '', request.POST['pass'])
		author = Author(user = user, points=5)
		author.save()
		user = authenticate(username=request.POST['username'], password=request.POST['pass'])
		login(request, user)
		return HttpResponseRedirect("/")

@login_required
def feedback(request, feedback_id):
	feedback = Feedback.objects.all().get(id=feedback_id)
	paper = feedback.paper
	fbAuthor = feedback.author
	pAuthor = paper.author
	myAuthor = Author.objects.all().get(user=request.user)
	notice = Notification(content="Your feedback for '"+paper.question+"' was given "+request.POST['points']+" points.", author=fbAuthor)
	notice.save()
	reward = int(request.POST['points'])
	paper.points -= reward
	fbAuthor.points += reward
	fbAuthor.save()
	feedback.chosen = True
	paper.save()
	return HttpResponseRedirect("/")

@login_required
def submitfeedback(request):
	paper = Paper.objects.all().get(id=request.POST['paper'])
	author = Author.objects.all().get(user=request.user)
	feedback = Feedback(content=request.POST['feedback'], author=Author.objects.all().get(user=request.user), paper=paper)
	feedback.save()
	notification = Notification(content=author.user.username+" submitted feedback on '"+paper.question+"'.", author=paper.author)
	notification.save()
	return HttpResponseRedirect("/edit/"+str(paper.id))

@login_required
def submit(request):
	template = loader.get_template('edit/submit.html')
	context = RequestContext(request, {
		'author': Author.objects.all().get(user=request.user)
	})

	return HttpResponse(template.render(context))

@login_required
def submitpaper(request):
	print request.POST['question']
	print request.POST['body']
	author = Author.objects.all().get(user = request.user)
	author.points -= int(request.POST['points'])
	print author.points
	sys.stdout.flush()
	author.save()
	paper = Paper(question = request.POST['question'], points = request.POST['points'], body = request.POST['body'], author=Author.objects.all().get(user=request.user), pub_date = timezone.now())
	paper.save()
	print paper.id
	return HttpResponseRedirect("/edit/"+str(paper.id))