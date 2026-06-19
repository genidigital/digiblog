from django.db import models
from admin_app.models import Category
    
class Article(models.Model):
    title = models.CharField(max_length=200)
    time_to_read = models.IntegerField()
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    counter = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    def increment_counter(self):
        self.counter+=1
        self.save()
    