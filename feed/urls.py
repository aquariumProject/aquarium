from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',FeedList.as_view()),
    #path('create/',FeedCreate.as_view()),
    path('<int:pk>/',FeedDetail.as_view()),
    path('<int:pk>/likes/', PostLikesAPIView.as_view(), name='likes'),
    path('reply',ReplyAPIView.as_view()),
    path('reply/<int:pk>',ReplyDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)