from django.urls import path
from .views import RegisterView, LoginView, ProfileView, FollowView, UnfollowView

from rest_framework.routers import DefaultRouter
from .views import UserViewSet


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("follow/<int:user_id>/", FollowView.as_view(), name="follow"),
    path("unfollow/<int:user_id>/", UnfollowView.as_view(), name="unfollow"),
]

router = DefaultRouter()
router.register(r'users', UserViewSet, basename="user")

urlpatterns = router.urls
