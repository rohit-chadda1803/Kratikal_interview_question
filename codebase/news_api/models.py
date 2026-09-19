from django.db import models

class Source(models.Model):
    name = models.CharField(max_length=255)
    reliability_score = models.FloatField(default=1.0)
    canonical_domain = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Story(models.Model):
    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('ACTIVE', 'Active'),
        ('BREAKING', 'Breaking'),
        ('COOLING', 'Cooling'),
        ('ARCHIVED', 'Archived'),
    ]
    canonical_title = models.CharField(max_length=500)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    source_count = models.IntegerField(default=1)
    score = models.FloatField(default=0.0)
    first_seen_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.canonical_title

class Article(models.Model):
    story = models.ForeignKey(Story, related_name='articles', on_delete=models.CASCADE, null=True, blank=True)
    source = models.ForeignKey(Source, related_name='articles', on_delete=models.CASCADE)
    canonical_url = models.URLField(unique=True)
    title = models.CharField(max_length=500)
    body = models.TextField()
    published_at = models.DateTimeField()

    def __str__(self):
        return self.title