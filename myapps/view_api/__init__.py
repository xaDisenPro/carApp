from rest_framework import routers

from view_api.art_api import TagViewSet
from view_api.tag_api import ArtViewSet

api_router = routers.DefaultRouter()

api_router.register(r'tag', TagViewSet)
api_router.register(r'art', ArtViewSet)
