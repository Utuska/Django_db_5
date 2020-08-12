from django.urls import path

from school.views import students_list
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', students_list, name='students'),
]
