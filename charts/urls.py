from django.conf.urls import url
from .views import view_charts, get_data

urlpatterns = [
      url(r'^$', view_charts, name='charts'),  
      url(r'^data/$', get_data, name='data'),  
]