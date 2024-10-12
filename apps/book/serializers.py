from django.utils.timezone import now
from rest_framework import serializers

from apps.book.models import Book, BookReview


class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Book
        # fields = '__all__'
        fields = ['poster_url', 'cover_url', 'title', 'author_name', 'release_date', 'rate', 'pages_count', 'tags']

    def get_tags(self, obj):
        return [tag.name for tag in obj.tags.all()]



class BookReviewSerializer(serializers.ModelSerializer):
    user_image = serializers.ImageField(source='user.image', read_only=True)
    user_full_name = serializers.CharField(source='user.full_name', read_only=True)
    days_since_created = serializers.SerializerMethodField()

    class Meta:
        model = BookReview
        fields = ['id', 'user_image', 'user_full_name', 'rating', 'days_since_created', 'comment']

    def get_days_since_created(self, obj):
        return (now() - obj.created).days