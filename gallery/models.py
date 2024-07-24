from django.db import models
from main.models import Content

class ContentImages(models.Model):
	content = models.ForeignKey(Content, verbose_name='Товар', related_name='images', on_delete=models.CASCADE)
	image = models.ImageField('Добавить фото',upload_to='content_images')
	alt_text = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return f"Фото для товара: {self.content}"
	
	class Meta:
		verbose_name = "Фото товара"
		verbose_name_plural = "Фото товаров"