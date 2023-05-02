from django.db import models

# Create your models here.

class Posting(models.Model):
    title = models.CharField('Title', max_length=50, blank=True)  
    upload_time = models.DateTimeField(unique=True)
    content = models.TextField('Content')

    def __str__(self):
        return self.title
    
class User(models.Model):
    username = models.CharField(max_length=64,verbose_name= '사용자명')
    password = models.CharField(max_length=64,verbose_name = '비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,verbose_name='등록시간')

    def __str__(self):
        return self.username


    class Meta:
        db_table = 'test_user'
    



