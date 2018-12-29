from django.conf.urls import url, include
from pages.views import issue_tracker
from .views import all_bugs, all_features, bug_detail, feature_detail, report_bug, suggest_feature, upvote_bug

urlpatterns = [
  url(r'^$', issue_tracker, name='tracker_home'),
  
  url(r'^all-bugs$', all_bugs, name='all_bugs'),
  url(r'^bug/(?P<pk>\d+)/$', bug_detail, name='bug_detail'),
  url(r'^report-bug$', report_bug, name='report_bug'),
  url(r'^upvote_bug/(?P<pk>\d+)/$', upvote_bug, name='upvote_bug'),
  
  url(r'^all_features$', all_features, name='all_features'),
  url(r'^feature/(?P<pk>\d+)/$', feature_detail, name='feature_detail'),
  url(r'^suggest-feature$', suggest_feature, name='suggest_feature'),
]