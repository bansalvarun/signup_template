from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from allauth.accounts.models import *
@login_required(login_url='/accounts/login/')
def profile(request):
  # user = get_object_or_404(Profile, pk=url)
  args ={}
  # args['user'] = user;
  allusers = Profile.objects.all()
  args['allusers'] = allusers
  return render(request, 'profile.html', args) 

def home(request):
	args = {}
	return render(request, 'index.html', args)