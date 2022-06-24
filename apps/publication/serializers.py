from dataclasses import fields
from rest_framework import serializers
from .models import Publication


class PublicationSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.nickname')
    created_at = serializers.DateTimeField(format='%d:%m:%Y %H:%M')
    update_at = serializers.DateTimeField(format='%d:%m:%Y %H:%M')
    views_count = serializers.ReadOnlyField()


    class Meta:
        model = Publication
        fields = ('author', 'title', 'content', 'created_at', 'update_at', 'views_count', 'category')

    def save(self, **kwargs):
        self.validated_data['author'] = self.context['request'].user
        return super().save(**kwargs)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['images'] = [{'image':image.image.url} for image in instance.pub_images.all()]
        return rep
