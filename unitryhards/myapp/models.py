from django.db import models
from django.contrib.auth.models import User

# University Model
class University(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

# Department Model
class Department(models.Model):
    name = models.CharField(max_length=255)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='departments')

    def __str__(self):
        return f'{self.name} ({self.university.name})'

# Course Model
class Course(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return f'{self.name} ({self.department.name})'

# Paper Model
class Paper(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="No description available")
    file = models.FileField(upload_to='papers/')  # Folder where the papers will be stored
    course = models.ForeignKey(Course, related_name='papers', on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_comments(self):
        from .models import Comment
        return Comment.objects.filter(paper=self)

 # Comment Model   
class Comment(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name="comments")  # Link to Paper model
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User model (if users should be able to comment)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.paper.title}"