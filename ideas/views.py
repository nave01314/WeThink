from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse

from django.template import loader

from .models import Idea
from .models import IdeaTag


def index(request):
    try:
        latest_idea_list = Idea.objects.order_by('-pub_date')[:5]
    except Idea.DoesNotExist:
        raise Http404("No ideas could be found.")
    context = {
        'latest_idea_list': latest_idea_list,
    }
    return HttpResponse(render(request, 'ideas/index.html', context))


def search_form(request):
    return render(request, 'ideas/search_form.html')


def search(request):
    relevant_idea_list = []
    latest_idea_list = Idea.objects.order_by('-pub_date')[:5]
    for r in latest_idea_list:
        if request.GET('q') in r.tags:
            relevant_idea_list.append(r)
        
    context = {
        'relevant_idea_list': relevant_idea_list
    }
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)


def detail(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)
    display_tags = ', '.join([t.IdeaTag for t in idea.tags])
    context = {
        'idea': idea,
    }
    return HttpResponse(render(request, 'ideas/detail.html', context))

