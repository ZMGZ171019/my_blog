from django.db import models
from django.urls import reverse


class Article(models.Model):
	title = models.CharField(max_length = 100, verbose_name = '标题')
	category = models.CharField(max_length = 50,blank = True, verbose_name = '标签')
	date_time = models.DateTimeField(auto_now_add = True, verbose_name = '时间')
	content = models.TextField(blank = True, null = True, verbose_name = '文章')
	
	def get_absolute_url(self):
		path = reverse('detail', kwargs={'id':self.id})
		return "http://127.0.0.1:8000%s" % path
	
	def __str__(self):
		return self.title
	
	class Meta:
		ordering = ['-date_time']
