from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Candidate, Poll, Choice

import datetime

def index(request):
    candidates = Candidate.objects.all()
    context = {'candidates':candidates}
    return render(request, 'elections/index.html', context)

def areas(request, area):
    today = datetime.datetime.now()
    try:
        poll = Poll.object.get(area = area, start_date__lte = today, end_date__gte = today)
        candidates = Candidate.objects.filter(area = area)
    except:
        poll = None
        candidates = None
    context = {'candidates':candidates, 'area':area, 'poll':poll}
    return render(request, 'elections/area.html', context)