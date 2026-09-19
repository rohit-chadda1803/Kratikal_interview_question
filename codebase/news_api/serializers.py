from rest_framework import serializers
from .models import Source, Story, Article

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ['id', 'name', 'reliability_score', 'canonical_domain']

class ArticleSerializer(serializers.ModelSerializer):
    source_name = serializers.ReadOnlyField(source='source.name')

    class Meta:
        model = Article
        fields = ['id', 'title', 'canonical_url', 'source_name', 'published_at']

class FeedStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'canonical_title', 'status', 'source_count', 'score', 'first_seen_at', 'last_updated_at']

class StoryDetailSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Story
        fields = ['id', 'canonical_title', 'status', 'source_count', 'score', 'first_seen_at', 'last_updated_at', 'articles']