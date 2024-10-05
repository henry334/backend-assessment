from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task_1/', include('task_1.urls')),
    path('task_2/', include('task_2.urls')),
    path('task_3/', include('task_3.urls')),
]
