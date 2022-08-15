from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    item_code=models.CharField(max_length=20,verbose_name='상품번호')
    item_name=models.CharField(max_length=100,verbose_name='상품명')   
    #item_manufacturer=models.CharField(max_length=10,verbose_name='제조사')
    item_price=models.CharField(max_length=20,verbose_name='상품가격')
    item_rate=models.CharField(max_length=20,verbose_name='할인율')
    item_link=models.URLField(verbose_name='링크')
    #item_like=models.ManyToManyField(User)
    #item_image=models.ImageField(upload_to='/',default='')

    



    

    




