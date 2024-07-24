from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	img = models.ImageField('Фото пользователя', default='default.png', upload_to='user_images')
	address = models.CharField(max_length=255, verbose_name='Адрес', default='Адрес не указан')
	phone_number = models.CharField(max_length=15, verbose_name='Номер телефона', default='Номер не указан')

	def __str__(self):
		return f'Профиль пользователя {self.user.username}'
    
	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		image = Image.open(self.img.path)

		if image.height > 256 or image.width > 256:
			resize = (256, 256)
			image.thumbnail(resize)
			image.save(self.img.path)
      
	class Meta:
		verbose_name = 'Профиль'
		verbose_name_plural = 'Профили'