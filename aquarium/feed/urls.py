from django.urls import path
from .views import FeedCreate, FeedDetail, FeedList, FeedLikes, PostLikesAPIView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('',FeedList.as_view()),
    path('<int:pk>',FeedDetail.as_view()),
    path('<int:pk>/likes/', PostLikesAPIView.as_view(), name='likes'),

]

urlpatterns = format_suffix_patterns(urlpatterns)