"""issue_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from .settings import MEDIA_ROOT
from django.conf.urls import url, include
from django.views import static
from django.contrib import admin
from pages.views import index, issue_tracker
from accounts import urls as accounts_urls
from products import urls as products_urls
from checkout import urls as checkout_urls
from issues import urls as issues_urls
from cart import urls as cart_urls
from charts import urls as charts_urls
from comments import urls as comments_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='home'),
    url(r'^issue-tracker/', include(issues_urls)),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^unicoins/', include(products_urls)),
    url(r'^cart/', include(cart_urls)),
    url(r'^checkout/', include(checkout_urls)),
    url(r'^charts/', include(charts_urls)),
    url(r'^comments/', include(comments_urls)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
    
]
