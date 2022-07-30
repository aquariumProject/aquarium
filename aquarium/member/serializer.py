from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('member_code', 'member_id', 'member_password', 'member_name',
        'member_nickname', 'member_email', 'member_gender', 'member_dob', 'member_join_date', 'member_pic')