from django.conf.urls import url
from .views import view_charts

urlpatterns = [
      url(r'^$', view_charts, name='charts'),  
]