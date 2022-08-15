from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from feed.serializers import FeedSerializer, PostLikeSerializer
from members.models import User
from feed.models import Feed
from members.permission import *
from django.http  import JsonResponse

from django.views.decorators.csrf import csrf_exempt

# feed 글 작성
@csrf_exempt
class FeedCreate(generics.CreateAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
   
    permission_classes = [
        IsAuthenticated,
    ]

   	# serializer.save() 재정의
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
        serializer.save()


# feed 글 목록 보기(post 방식)
class FeedList(generics.ListCreateAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    permission_classes = [
        AllowAny,
    ]


# feed 글 내용 보기(get 방식)
class FeedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    permission_classes = [
        IsAuthorOrReadonly,
    ]

    # def likes(request, feed_code):
    #     if request.user.is_authenticated:
    #         feed = get_object_or_404(Feed, pk=feed_code)

    #         if feed.like_users.filter(pk=request.user.pk).exists():
    #             feed.like_users.remove(request.user)
    #             return JsonResponse({'message': 'success'}, status=200)
    #         else:
    #             feed.like_users.add(request.user)
    #             return JsonResponse({'message': 'failed'}, status=200)

class FeedLikes(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feed.objects.all()
    serializer_class = PostLikeSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    # def likes(request, feed_code):
    #     if request.user.is_authenticated:
    #         feed = get_object_or_404(Feed, pk=feed_code)

    #         if feed.like_users.filter(pk=request.user.pk).exists():
    #             feed.like_users.remove(request.user)
    #             return JsonResponse({'message': 'success'}, status=200)
    #         else:
    #             feed.like_users.add(request.user)
    #             return JsonResponse({'message': 'failed'}, status=200)

class PostLikesAPIView(generics.UpdateAPIView):
    queryset = Feed.objects.all()
    serializer_class = PostLikeSerializer

    permission_classes = [
        IsAuthenticated,
    ]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        feed_like = {'feed_like' : instance.feed_like + 1}
        serializer = self.get_serializer(instance, data=feed_like, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefeched_objects_cache = {}

        return Response(serializer.data)