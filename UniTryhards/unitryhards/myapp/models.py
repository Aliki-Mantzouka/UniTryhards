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

    CATEGORY_CHOICES = [
    ('notes', 'Notes'),
    ('exams', 'Past Exam Questions'),
    ('general', 'General'),
]
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='general')

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
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.paper.title}"

# Favourite Papers Model  
class FavoritePaper(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'paper')

# Paper Report Model
class PaperReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paper = models.ForeignKey('Paper', on_delete=models.CASCADE)
    reason = models.TextField(blank=True)
    reported_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report by {self.user.username} on Paper ID {self.paper.id}"

# User Profile Model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_papers = models.ManyToManyField('Paper', blank=True, related_name='favorited_by')

    def __str__(self):
        return self.user.username