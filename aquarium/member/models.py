from django.db import models

class Member(models.Model):
    member_code = models.AutoField(primary_key=True)
    member_id = models.CharField(max_length=20)
    member_password = models.CharField(max_length=25)
    member_name = models.CharField(max_length=10)
    member_nickname = models.CharField(max_length=10)
    member_email = models.CharField(max_length=35)
    member_gender = models.CharField(max_length=1, blank=True, null=True)
    member_dob = models.DateField(blank=True, null=True)
    member_pic = models.CharField(max_length=100, blank=True, null=True)

class Test(models.Model):
    member_code = models.AutoField(primary_key=True)
    member_id = models.CharField(max_length=20)
    member_password = models.CharField(max_length=25)
    member_name = models.CharField(max_length=10)
    member_nickname = models.CharField(max_length=10)
    member_email = models.CharField(max_length=35)
    member_gender = models.CharField(max_length=1, blank=True, null=True)
    member_dob = models.DateField(blank=True, null=True)
    member_pic = models.CharField(max_length=100, blank=True, null=True)

class Member2(models.Model):
    test_col1 = models.CharField(primary_key=True, max_length=10)
    test_col2 = models.CharField(max_length=20)
    test_col3 = models.IntegerField(blank=True, null=True)