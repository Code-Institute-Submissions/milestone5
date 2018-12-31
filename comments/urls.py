from django.conf.urls import url
from .views import add_comment

urlpatterns = [ 
      url(r'^add/$', add_comment, name='add_comment'),  
]