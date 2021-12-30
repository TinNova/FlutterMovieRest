from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, UserViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'users', UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

"""
This is what the urlpatterns look like with views instead of viewsets,
it's more code, and more explicit. The negative is that we can customise
our endpoint and therefore drift away from standardised url practises
"""
# urlpatterns = [
#     path('movies/', MovieViewSet.as_view()),
#     path('movies/<int:pk>/', MovieViewSet.as_view()),
#     path('users/', UserList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view())
# ]
