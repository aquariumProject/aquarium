from rest_framework import serializers
from .models import Feed

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model=Feed
        fields=('id', 'title','content','date')

        