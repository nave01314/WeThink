from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse

from django.template import loader

from .models import Idea


def index(request):
    try:
        latest_idea_list = Idea.objects.order_by('-pub_date')[:5]
    except Idea.DoesNotExist:
        raise Http404("No ideas could be found.")
    context = {
        'latest_idea_list': latest_idea_list,
    }
    return HttpResponse(render(request, 'ideas/index.html', context))


def search(request):
    return HttpResponse(render(request, 'ideas/search.html'))


def detail(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)
    display_tags = ', '.join([t.IdeaTag for t in idea.tags])
    context = {
        'idea': idea,
    }
    return HttpResponse(render(request, 'ideas/detail.html', context))

