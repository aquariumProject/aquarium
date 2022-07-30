from django.db import models

class Jul26(models.Model):
    member_code = models.AutoField(primary_key=True)
    member_id = models.CharField(max_length=20)
    member_password = models.CharField(max_length=25)
    member_name = models.CharField(max_length=10)
    member_nickname = models.CharField(max_length=10)
    member_email = models.CharField(max_length=35)
    member_gender = models.CharField(max_length=1, blank=True, null=True)
    member_dob = models.DateField(blank=True, null=True)
    member_pic = models.CharField(max_length=100, blank=True, null=True)

class Jul27(models.Model):
    class META : 
        db_table = 'JUL26-2'
    member_code = models.AutoField(primary_key=True)
    member_id = models.CharField(max_length=20)
    member_password = models.CharField(max_length=25)
    member_name = models.CharField(max_length=10)
    member_nickname = models.CharField(max_length=10)
    member_email = models.CharField(max_length=35)
    member_gender = models.CharField(max_length=1, blank=True, null=True)
    member_dob = models.DateField(blank=True, null=True)
    member_pic = models.CharField(max_length=100, blank=True, null=True)

class july(models.Model):
    class META : 
        db_table = 'july'
    member_code = models.AutoField(primary_key=True)
    member_id = models.CharField(max_length=20)
    member_password = models.CharField(max_length=25)
    member_name = models.CharField(max_length=10)
    member_nickname = models.CharField(max_length=10)
    member_email = models.CharField(max_length=35)
    member_gender = models.CharField(max_length=1, blank=True, null=True)
    member_dob = models.DateField(blank=True, null=True)
    member_pic = models.CharField(max_length=100, blank=True, null=True)