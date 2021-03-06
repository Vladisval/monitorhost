from django.conf.urls import url
from main import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index),

    url(r'panel/$', views.panel, name='panel'),
    url(r'panel/chats/$', views.chats, name='chats'),
    url(r'panel/chat/(?P<id>.+)/$', views.chat, name='chat'),
    url(r'panel/profile/$', views.profile, name='profile'),
    url(r'panel/servers/$', views.servers, name='servers'),
    url(r'panel/serversforsale/$', views.servers_for_sale, name='servers_for_sale'),


    #user settings
    url(r'panel/profile/img', views.load_user_img, name='load_user_img'),
    #url(r'panel/messages/$', views.panel_write_message, name='write_message'),

    url(r'panel/buyserver/(?P<id>.+)/$', views.buy_server, name='buy_server'),
    url(r'login/$', views.log_in, name='login'),
    url(r'registration/$', views.register, name='reg'),
    url(r'logout/$', views.log_out, name='logout'),
    url(r'activate/(?P<username>.+)/(?P<code>.+$)', views.activate, name='activate'),
    url(r'recovery/$', views.recovery, name='pass_recovery'),
    url(r'recovery/(?P<username>.+)/(?P<code>.+$)', views.change_pass, name='change_pass'),

    url(r'check-data/$', views.check),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
