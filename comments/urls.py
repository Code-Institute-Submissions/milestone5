from django.conf.urls import url
from .views import add_bug_comment, add_feature_comment

urlpatterns = [ 
      url(r'^add-bug-comment/(?P<pk>\d+)/$', add_bug_comment, name='add_bug_comment'),  
      url(r'^add-feature-comment/(?P<pk>\d+)/$', add_feature_comment, name='add_feature_comment'),  
]