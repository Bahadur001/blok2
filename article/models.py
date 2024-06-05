from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=150, verbose_name="kitab_name")
    content = RichTextField(verbose_name="subject")
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to='images', null=True, blank=True, verbose_name="Sekil")
    
    def __str__(self):
        return f"{self.title} | {self.author}"
