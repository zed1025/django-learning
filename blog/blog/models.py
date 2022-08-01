from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey(
		'auth.User', # many-to-one, one user can be author of many posts
		on_delete = models.CASCADE,
	)
	body = models.TextField()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post_detail', args=[str(self.id)]) # 'pk' and 'id' can be used interchangably
