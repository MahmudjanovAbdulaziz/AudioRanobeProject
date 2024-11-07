from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static


from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('slug-title/', book_page, name='book_page')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
