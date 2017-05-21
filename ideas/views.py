from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse
from django.utils import timezone
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
    return render(request, 'ideas/index.html', context)


def profile(request):
    return render(request, 'ideas/profile.html')

def submit_idea(request):
    if 'i' in request.POST:
        i = Idea(idea_text=request.POST['i'], pub_date=timezone.now())
        i.save()
        if 't' in request.POST:
            t = IdeaTag(tag_text=request.POST['t'])
            t.save()
            i.tags.add(t)
        i.save()
    
    return render(request, 'ideas/profile.html')
    

def search_form(request):
    return render(request, 'ideas/search_form.html')


def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
        idea_list = Idea.objects.filter(tags__tag_text__startswith=request.GET['q'])
    else:
        message = 'You submitted an empty form.'
                
    context = {
        'message': message,
        'relevant_idea_list': idea_list
    }
    return render(request, 'ideas/search_form.html', context)


def detail(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)
    display_tags = idea.tags.all()
    context = {
        'idea': idea,
        'display_tags': display_tags
    }
    return render(request, 'ideas/detail.html', context)

