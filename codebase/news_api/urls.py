from django.urls import path
from .views import FeedView, StoryDetailView, StorySourcesView

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
    path('story/<int:pk>/', StoryDetailView.as_view(), name='story-detail'),
    path('story/<int:pk>/sources/', StorySourcesView.as_view(), name='story-sources'),
]