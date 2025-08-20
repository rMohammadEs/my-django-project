from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.blog'
    verbose_name = 'مدیریت مقالات و نوشته‌ها'

    def ready(self):
        print("برنامه وبلاگ با موفقیت راه‌اندازی شد!")