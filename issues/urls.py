from django.conf.urls import url, include
from pages.views import issue_tracker
from .views import all_bugs_fixed, all_bugs_working, all_bugs_todo, all_features_added, all_features_working, all_features_pending, bug_detail, feature_detail, report_bug, suggest_feature, upvote_bug, bug_fixed, upvote_feature

urlpatterns = [
  url(r'^$', issue_tracker, name='tracker_home'),
  
  url(r'^all-bugs/fixed$', all_bugs_fixed, name='all_bugs_fixed'),
  url(r'^all-bugs/working-on$', all_bugs_working, name='all_bugs_working'),
  url(r'^all-bugs/todo$', all_bugs_todo, name='all_bugs_todo'),
  url(r'^bug/(?P<pk>\d+)/$', bug_detail, name='bug_detail'),
  url(r'^report-bug$', report_bug, name='report_bug'),
  url(r'^upvote-bug/(?P<pk>\d+)/$', upvote_bug, name='upvote_bug'),
  url(r'^bug-fixed/(?P<pk>\d+)/$', bug_fixed, name='bug_fixed'),
  
   url(r'^all-features/added$', all_features_added, name='all_features_added'),
  url(r'^all-features/working-on$', all_features_working, name='all_features_working'),
  url(r'^all-features/pending$', all_features_pending, name='all_features_pending'),
  url(r'^feature/(?P<pk>\d+)/$', feature_detail, name='feature_detail'),
  url(r'^suggest-feature$', suggest_feature, name='suggest_feature'),
  url(r'^upvote-feature/(?P<pk>\d+)/$', upvote_feature, name='upvote_feature'),
]