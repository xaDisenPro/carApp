from rest_framework import serializers, viewsets
from art.models import Art


class ArtSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Art
        fields = ('title', 'summary', 'content', 'tag', 'tagName')


class ArtViewSet(viewsets.ModelViewSet):
    queryset = Art.objects.all()
    serializer_class = ArtSerializer

