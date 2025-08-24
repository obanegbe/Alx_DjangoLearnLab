from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="post")
router.register(r"comments", CommentViewSet, basename="comment")

urlpatterns = [
    path("", include(router.urls)),
    path("feed/", views.FeedView.as_view(), name="feed"), 
    router.urls
]

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename="post")
