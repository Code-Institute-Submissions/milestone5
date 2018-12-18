from django.conf.urls import url, include
from accounts.views import logout, login


urlpatterns = [
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
]