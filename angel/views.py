from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


@login_required
def home(request, template):
    context = {}

    return render(request, template, context)


def about(request, template):
    context = {}

    return render(request, template, context)