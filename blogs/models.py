from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    picture = models.FileField()
    category = models.CharField(max_length=20, choices=(
        ("AI", "Artificial Intelligence"),
        ("IT", "Information Technology"),
        ("CN", "Computer Network"),
        ("PROGRAMMING", "Programming"),
        ('OS', "Operating Systems"),
        ("ROBOTICS", "Robotics"),
        ("QC", "Quantum Computing"),
        ("DS", "Data Science"),
        ("AUTOMATION", "Automation"),
        ("VR", "Virtual Reality"),
    ), default=None)
    datetime = models.DateTimeField(auto_now_add=True)
    heading = models.CharField(max_length=120)
    content = RichTextField()
    def __str__(self):
        return self.heading


class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="Comments")
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['pk']


