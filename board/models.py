from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    author = models.CharField(max_length=20)
    view = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def update_counter(self):
        self.view += 1
        self.save()

    def summary(self):
        return self.content[:30]
