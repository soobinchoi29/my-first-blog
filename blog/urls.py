from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static


urlpatterns = [ 
	path('', views.index),
	path('index', views.index),

	path('form', views.post),
	path('', views.post),

	path('', views.result),

	path('analysis', views.analysis),
	path('chatbot', views.chatbot),


	#url(r'^names/(?P<name>.+)/$', views.names),
	#url(r'^admin/$', views.post),
	#path('',views.first),
]
