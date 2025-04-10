from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.IntegerField(help_text='Duration in hours')
    thumbnail = models.ImageField(upload_to="course_thumbnails/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.duration} hrs)"

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    video_url = models.URLField(null=True, blank=True)
    completion_status = models.BooleanField(default=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')

    def __str__(self):
        return f"{self.title} - {self.course.title}"

class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    enrolled_courses = models.ManyToManyField(Course, related_name='students')
    completed_lessons = models.ManyToManyField(Lesson, related_name='completed_by', blank=True)

    def __str__(self):
        return f"{self.name} ({self.email})"
