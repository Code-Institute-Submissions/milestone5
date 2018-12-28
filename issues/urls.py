from django.conf.urls import url, include
from pages.views import issue_tracker

urlpatterns = [
      url(r'^$', issue_tracker, name='tracker_home'),  
]