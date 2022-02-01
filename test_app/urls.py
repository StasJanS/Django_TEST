from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import index, user_login, user_logout, user_register, all_short_url, del_file

urlpatterns = [
                  path('', index, name='index'),
                  path('login/', user_login, name='login'),
                  path('register/', user_register, name='register'),
                  path('logout/', user_logout, name='logout'),
                  path('all_short_url/', all_short_url, name='all_short_url'),
                  path('del/', del_file, name='del_file'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
