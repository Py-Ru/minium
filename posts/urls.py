from django.urls import path
from .views import (
    PostDetailView,
    PostListCreateView,
    CommentListCreateView,
    CommentDetailView,
)

urlpatterns = [
    path('', PostListCreateView.as_view()),
    path('<slug:slug>/', PostDetailView.as_view()),
    path('<slug:slug>/comments/', CommentListCreateView.as_view()),
    path('comments/<int:pk>/', CommentDetailView.as_view()),
]
