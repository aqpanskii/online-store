from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Content(models.Model):
	material_number = models.CharField(
		"Номер материала", max_length=10, unique=True, default="000-00000"
	)
	title = models.CharField(
		"Mатериал", max_length=100
	)
	text = models.TextField(
		"Oписание материала"
	)
	date = models.DateTimeField(
		"Скидка действительна до", blank=True, null=True
	)
	price = models.DecimalField(
		"Цена", max_digits=10, decimal_places=2
	)
	old_price = models.DecimalField(
		"Старая цена", max_digits=10, decimal_places=2, blank=True, null=True
	)
	avtor = models.ForeignKey(
		User, verbose_name='Автор', on_delete=models.CASCADE
	)
	# is_active = models.BooleanField(default=True)
	img_content = models.ImageField('Фото товара', default='default_content.png', upload_to='content_images')

	ar_content_gltf = models.FileField('AR document (.gltf)', upload_to='content_ar', null=True, blank=True)
	ar_content_bin = models.FileField('AR document (.bin)', upload_to='content_ar', null=True, blank=True)
	ar_content_texture = models.FileField('AR document (.jpg)', upload_to='content_ar', null=True, blank=True)
	# sizes = (
	# 	('S', 'Small'),
	# 	('M', 'Medium'),
	# 	('L', 'Large'),
	# 	('XL', 'X Large'),
	# )
	# shop_sizes = models.CharField(max_length=2, choices=sizes, default='M')

	def get_absolute_url(self):
		return reverse('content-detail', kwargs={'pk':self.pk})

	def __str__(self):
		return f"Товар: {self.material_number}"

	class Meta:
		verbose_name = "Товар"
		verbose_name_plural = "Товары"



