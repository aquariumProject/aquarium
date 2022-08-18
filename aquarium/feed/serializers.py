from dataclasses import fields
from pyexpat import model
from .models import Reply
from members.serializers import RegisterSerializer
from feed.models import Feed
from members.models import User
from rest_framework import serializers

class FeedSerializer(serializers.ModelSerializer):
    #member_id = serializers.ReadOnlyField(source = 'user.member_id')
    # member_id = RegisterSerializer(many=True, read_only=True)
    class Meta:
        model = Feed
        fields = ['feed_code', 'member_id', 'feed_title', 'feed_content', 'feed_pic', 'feed_date', 'feed_like', 'feed_hit']

class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ['feed_like']

class ReplySerializer(serializers.ModelSerializer):
    #member_id = serializers.ReadOnlyField(source = 'user.member_id')
    class Meta:
        model = Reply
        fields = ['feed_reply_code', 'feed_code', 'member_id', 'feed_reply_content', 'feed_date']