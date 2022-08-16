from django.db import models
from members.models import User

class Feed(models.Model):
    feed_code = models.AutoField(primary_key=True, null=False, blank=False)
    member_id = models.ForeignKey(User, related_name='member_id', null=False, blank=False, on_delete=models.CASCADE, db_column='member_id') # 사용자 정보가 삭제될 경우 글도 삭제
    member_id = models.CharField(max_length=20)
    feed_title = models.CharField(max_length=50)
    feed_content = models.TextField()
    feed_pic = models.ImageField(null=True, upload_to='uploads', blank=True)
    feed_date = models.DateTimeField(auto_now_add=True)
    feed_like = models.ManyToManyField(User, related_name='likes', blank=True, default=0)
    feed_like = models.IntegerField(default=0)
    feed_hit = models.PositiveBigIntegerField(default=0)