from django.urls import path
from petstagram.common import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('like/<int:photo_id>/', views.likes_functionality, name='like'),
    path('share/<int:photo_id>/', views.share_funcitonality, name='share'),
    path('comment/<int:photo_id>/', views.add_comment, name='comment'),

]
# comment_functionality
