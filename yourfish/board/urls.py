from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import FeedDetail,FeedList

urlpatterns=[
    path('feed/',FeedList.as_view()),
    path('feed/<int:pk>/',FeedDetail.as_view()),
]

# url 형식 접미사 패턴을 포함하는 url 패턴 list를 반환한다. 
# view에 format 키워드를 추가해야한다. 
urlpatterns=format_suffix_patterns(urlpatterns)