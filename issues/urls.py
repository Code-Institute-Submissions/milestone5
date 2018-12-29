from django.conf.urls import url, include
from pages.views import issue_tracker
from .views import report_bug, suggest_feature

urlpatterns = [
  url(r'^$', issue_tracker, name='tracker_home'),
  url(r'^report-bug$', report_bug, name='report_bug'),
  url(r'^suggest-feature$', suggest_feature, name='suggest_feature'),
]