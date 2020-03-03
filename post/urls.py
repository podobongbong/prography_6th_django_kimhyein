from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='post-list'),
    url(r'^(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='post-detail'),
    url(r'^create/$', views.PostCreateView.as_view(), name='post-create'),
    url(r'^(?P<pk>\d+)/edit/$', views.PostEditView.as_view(), name='post-edit'),
    url(r'^(?P<pk>\d+)/delete/$', views.PostDeleteView.as_view(), name='post-delete'),
]
