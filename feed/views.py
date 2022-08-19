from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from feed.serializers import FeedSerializer, PostLikeSerializer, ReplySerializer
from members.models import User
from feed.models import Feed, Reply
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
        serializer.save(member_id = self.request.member_id)
        serializer.save()


# feed 글 목록 보기(get 방식)
class FeedList(generics.ListCreateAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    permission_classes = [
        IsAuthenticated,
    ]


# feed 글 내용 보기, 수정, 삭제(post 방식)
class FeedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    permission_classes = [
        AllowAny,
    ]

    def get(self, request, pk):
        feed = Feed.objects.get(feed_code=pk)
        feed.feed_hit += 1
        feed.save()
        return Response(status=status.HTTP_200_OK)


    # 수정
    # def put(self, request, pk, format=None):
    #     feed = self.get_object(pk)
    #     serializer = FeedSerializer(feed, data=request.data) 
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data) 
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # # 삭제
    # def delete(self, request, pk, format=None):
    #     print("****************************")
    #     print(self.get_object(pk))
    #     feed = self.get_object(pk)
    #     feed.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)    


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


# 댓글 관련
class ReplyAPIView(generics.CreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

    permission_classes = [
        IsAuthenticated,
    ]

    def perform_create(self, serializer):
        #serializer.save(user = self.request.user)
        serializer.save()

class ReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

    permission_classes = [
        IsAuthorOrReadonly,
    ]