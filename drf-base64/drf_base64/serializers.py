from drf_extra_fields.fields import Base64ImageField, Base64FileField
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from .fields import Base64WithFilenameImageField, Base64WithFilenameFileField
from .models import SampleBase64ImageModel, SampleBase64FileModel, SampleParentModel


class SampleBase64ImageSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        model = SampleBase64ImageModel
        fields = (
            'id',
            'image',
        )


class SampleBase64FileSerializer(serializers.ModelSerializer):
    file = Base64FileField(required=False, allow_null=True)

    class Meta:
        model = SampleBase64FileModel
        fields = (
            'id',
            'file',
        )


class SampleBase64WithFilenameImageSerializer(serializers.ModelSerializer):
    image = Base64WithFilenameImageField(required=False, allow_null=True)

    class Meta:
        model = SampleBase64ImageModel
        fields = (
            'id',
            'image',
        )


class SampleBase64WithFilenameFileSerializer(serializers.ModelSerializer):
    file = Base64WithFilenameFileField(required=False, allow_null=True)

    class Meta:
        model = SampleBase64FileModel
        fields = (
            'id',
            'file',
        )


class SampleParentFilenameImageSerializer(WritableNestedModelSerializer):
    image_set = SampleBase64WithFilenameImageSerializer(many=True)

    class Meta:
        model = SampleParentModel
        fields = (
            'id',
            'image_set',
        )


class SampleParentFilenameFileSerializer(WritableNestedModelSerializer):
    file_set = SampleBase64WithFilenameFileSerializer(many=True)

    class Meta:
        model = SampleParentModel
        fields = (
            'id',
            'file_set',
        )
