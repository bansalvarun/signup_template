from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required

def home(request):
	args = {}
	return render(request, 'index.html', args)