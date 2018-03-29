from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index),
	url(r'^register',views.register),
    url(r'^landing',views.landing),
    url(r'^login', views.login),
    url(r'^logout',views.logout),
	url(r'^add_item', views.add_item),
	url(r'^wish_items', views.wish_items),
	url(r'^remove',views.remove),

]
