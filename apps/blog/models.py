from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    content = models.TextField(verbose_name="متن")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")
    published_date = models.DateTimeField(default=timezone.now, verbose_name="تاریخ انتشار")
    image = models.ImageField(upload_to='blog/images/', blank=True, null=True, verbose_name="تصویر")



    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست‌ها"
        ordering = ['-published_date']