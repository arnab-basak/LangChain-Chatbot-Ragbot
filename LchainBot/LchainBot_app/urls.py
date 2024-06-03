from django.urls import path
from . import views

#urlpatterns=[
#    path('', views.chat_view, name='chat_view'),
#    path('', views.ajax_chat, name='ajax_chat'),
#]

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('get_response/', views.get_response, name='get_response'),
]