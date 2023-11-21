from django.urls import path
from .views import dynamic_page, post_page, content_page, detail_page

urlpatterns = [
    path('dynamic/', dynamic_page, name='dynamic_page'),
    path('post/', post_page, name='post_page'),
    path('content/', content_page, name='content_page'),
    path('detail/', detail_page, name='detail_page'),
]