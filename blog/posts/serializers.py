from rest_framework import serializers
from .models import Post



SEARCH_PATTERN = '/media/content/ckeditor/'
SITE_DOMAIN = "http://127.0.0.1:8000"
REPLACE_WITH = "%s/media/content/ckeditor/" % SITE_DOMAIN


class FixAbsolutePathSerializer(serializers.Field):

    def to_representation(self, value):
        
        text = value.replace(SEARCH_PATTERN, REPLACE_WITH)
        return text



class ListPostSerialzier(serializers.ModelSerializer):
    content = FixAbsolutePathSerializer()
    class Meta:
        model = Post 
        fields = '__all__'