from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


@login_required
def home(request, template):
    context = {}
    return HttpResponseRedirect('/outfits/create/')
    #return render(request, template, context)


def about(request, template):
    context = {}
    return HttpResponseRedirect('/login/')
    # return render(request, template, context)


def friends(request):
    return render(request, 'friends.html')