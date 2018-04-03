from django.contrib import admin
# Register your models here.
from .models import Course, Lesson, Video, CourseResource
admin.site.register(Course,)
admin.site.register(Lesson, )
admin.site.register(Video,)
admin.site.register(CourseResource, )