from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('get/', views.getBlogs, name='get'),
    path('post/', views.postBlogs, name='post'),
    path('put/<int:pk>',views.putBlog, name='put'),
    path('delete/<int:pk>', views.deleteBlog, name='delete')
]