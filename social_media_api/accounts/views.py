from django.shortcuts import get_object_or_404

from rest_framework import status, permissions, viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from .models import CustomUser   # ✅ use your custom user model


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response(
                {"token": token.key, "user": UserSerializer(user, context={"request": request}).data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            token, _ = Token.objects.get_or_create(user=user)
            return Response(
                {"token": token.key, "user": UserSerializer(user, context={"request": request}).data},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user, context={"request": request}).data)

    def patch(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ Follow/Unfollow with CustomUser
class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()   # ✅
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target = get_object_or_404(CustomUser, pk=user_id)
        if target == request.user:
            return Response({"detail": "You cannot follow yourself."}, status=400)
        request.user.following.add(target)
        return Response({"detail": f"You now follow {target.username}."}, status=200)


class UnfollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()   # ✅
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target = get_object_or_404(CustomUser, pk=user_id)
        request.user.following.remove(target)
        return Response({"detail": f"You unfollowed {target.username}."}, status=200)


# ✅ ViewSet with CustomUser
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()   # ✅
    serializer_class = UserSerializer

    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def follow(self, request, pk=None):
        target_user = self.get_object()
        request.user.following.add(target_user)
        return Response({"detail": f"You are now following {target_user.username}"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def unfollow(self, request, pk=None):
        target_user = self.get_object()
        request.user.following.remove(target_user)
        return Response({"detail": f"You unfollowed {target_user.username}"}, status=status.HTTP_200_OK)
