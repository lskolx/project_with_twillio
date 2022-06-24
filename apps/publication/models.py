from datetime import datetime
from apps.category.models import Category
from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify

User = get_user_model()

class Publication(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_pub', verbose_name='Author')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank= True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    views_count = models.PositiveIntegerField(default=0)
    published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='publications', null=True)

    def __str__(self) -> str:
        return f'{self.title} from {self.author.nickname}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Publication, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-created_at']


class PublicationImage(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='pub_images')
    image = models.ImageField(upload_to='publication_images')

    def __str__(self):
        return self.publication.title + datetime.now().strftime('%Y:%m_%d')
    



