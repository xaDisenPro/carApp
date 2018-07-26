from rest_framework import serializers, viewsets
from art.models import Tag


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', 'modify_time')


class TagViewSet(viewsets.ModelViewSet):
    queryset =  Tag.objects.all()
    serializer_class = TagSerializer
