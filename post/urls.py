from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^create/$', views.PostCreateView.as_view(), name='post_create'),
    url(r'^(?P<pk>\d+)/edit/$', views.PostEditView.as_view(), name='post_edit'),
    url(r'^(?P<pk>\d+)/delete/$', views.PostDeleteView.as_view(), name='post_delete'),
]
