
from django.conf.urls import url, include
from django.contrib import admin
admin.site.site_header = 'AUTO-WEBSITE-ANALYSIS administration'
admin.site.site_title = 'AUTO-WEBSITE-ANALYSIS site admin'




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^website_analysis/',include('api.urls') )

]
