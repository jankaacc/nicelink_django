from django.conf.urls import url


from . import views

app_name = 'nicelink'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^link_list/$', views.link_list, name='link_list'),
    url(r'^user/$', views.register_view, name='register_view'),
    url(r'^login/$', views.login_view, name='login_view'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^link/(?P<original_link>.+)/$', views.redirect_to_oryginal_link, name='redirect_to_oryginal_link'),
    ]
# (?P<oryginal_link>)/