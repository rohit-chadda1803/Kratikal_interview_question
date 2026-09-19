from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Story, Source
from .serializers import FeedStorySerializer, StoryDetailSerializer, SourceSerializer

class FeedView(generics.ListAPIView):
    """GET /api/feed/ - Paginated ranked story feed"""
    queryset = Story.objects.all().order_by('-score', '-last_updated_at')
    serializer_class = FeedStorySerializer

class StoryDetailView(generics.RetrieveAPIView):
    """GET /api/story/{id}/ - Full story details with articles"""
    queryset = Story.objects.all()
    serializer_class = StoryDetailSerializer

class StorySourcesView(APIView):
    """GET /api/story/{id}/sources/ - Independent sources for a story"""
    def get(self, request, pk):
        try:
            story = Story.objects.get(pk=pk)
        except Story.DoesNotExist:
            return Response({"error": "Story not found"}, status=status.HTTP_404_NOT_FOUND)
        
        sources = Source.objects.filter(articles__story=story).distinct()
        serializer = SourceSerializer(sources, many=True)
        return Response({
            "story_id": story.id,
            "independent_source_count": sources.count(),
            "sources": serializer.data
        })