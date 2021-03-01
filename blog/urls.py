from django.urls import path, include
from . import views
from .api import views as api_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', api_views.PostViewSet)

app_name = 'blog'
urlpatterns = [
    path('v1/', include(router.urls)),
    path('', views.PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('like/', views.like_post, name='like-post'),
    path('user/<str:username>', views.UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('latest/', views.PostLatestView.as_view(), name='post-latest'),
]
