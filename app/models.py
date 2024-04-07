from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Games(models.Model):
    class Meta:
        verbose_name_plural = "Games"
    title = models.CharField(max_length=100, verbose_name="title")
    description = models.TextField(verbose_name="description")
    publisher = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    created_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    picture = models.ImageField(verbose_name="picture",blank=True)
    # color = models.TextField(verbose_name="color")
    def get_absolute_url(self):
        return reverse("g_path", args=[self.slug])
    
    #через admin_panel добавить игры