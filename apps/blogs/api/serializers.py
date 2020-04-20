from rest_framework import serializers
from blogs.models import Blog
from metas.api.serializers import MetaSerializers
# Spider.crawl_page(threading.currentThread().name, url)


class BlogSerializer(serializers.ModelSerializer):
    meta = MetaSerializers()

    class Meta:
        model = Blog
        fields = '__all__'

    def create(self, validated_data):
        meta_data = validated_data.pop('meta')
        meta = MetaSerializers.create(
            MetaSerializers(), validated_data=meta_data)
        validated_data['meta'] = meta
        blog_created = Blog.objects.create(**validated_data)
        return blog_created

    # def get_more_filed(self, obj):
    #     return "1aaaaa"
