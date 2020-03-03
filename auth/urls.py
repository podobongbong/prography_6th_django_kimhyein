from django.conf.urls import url
from django.urls import include


urlpatterns = [
    url(r'registration/', include('rest_auth.registration.urls')),
    url(r'', include('rest_auth.urls')),
]
