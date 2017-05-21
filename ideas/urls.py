from django.conf.urls import url

from . import views

app_name = 'ideas'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^submit_idea/$', views.submit_idea, name='submit_idea'),
    url(r'^search-form/$', views.search_form, name='search_form'),
    url(r'^search/$', views.search, name='search'),
    url(r'^(?P<idea_id>[0-9]+)/$', views.detail, name='detail'),
]