from django.db import models

# Create your models here.
class NFT(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)


class User(models.Model):
    pass


# docker-compose exec backend sh
# python manage.py makemigrations
# python manage.py migrate
