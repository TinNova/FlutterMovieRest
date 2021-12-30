from .models import FavouriteMovie
from .permissions import IsOwner
from .serializers import FavouriteMovieSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.contrib.auth.models import User
from flutter_movie_rest.serializers import UserSerializer


# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    and `destroy` actions, but not 'update'.
    """
    queryset = FavouriteMovie.objects.all()
    serializer_class = FavouriteMovieSerializer
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # List is filtered to only show the owners movies
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class MovieList(generics.ListCreateAPIView):
#     queryset = FavouriteMovie.objects.all()
#     serializer_class = FavouriteMovieSerializer
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#
#
# class MovieDetail(generics.RetrieveDestroyAPIView):
#     queryset = FavouriteMovie.objects.all()
#     serializer_class = FavouriteMovieSerializer
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
