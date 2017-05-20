from django.shortcuts import render

from django.http import HttpResponse
from django.http import Http404
from django.template import loader

from .models import Idea


def index(request):
    latest_idea_list = Idea.objects.order_by('-pub_date')[:5]
    context = {
        'latest_idea_list': latest_idea_list,
    }
    return HttpResponse(render(request, 'ideas/index.html', context))


def detail(request, idea_id):
    try:
        idea = Idea.objects.get(id=idea_id)
    except Idea.DoesNotExist:
        raise Http404("Idea does not exist")

    context = {
        'idea': idea,
    }
    return HttpResponse(render(request, 'ideas/detail.html', context))

