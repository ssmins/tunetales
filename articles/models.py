from django.db import models

# Create your models here.
class Article(models.Model): 
    # 어떤 정보를 입력받을까 
    # 1) 노래 제목 
    # 2) spotify에서 검색 
    # 3) 사연 작성하기 
    # form 이 나머지(created_at, updated_at은 작성해 주나 ?)
    song_title = models.CharField(max_length=50) 
    # search_spotify 
    song_url = models.URLField(blank=True , null=True) # spotify 곡 추가할 곳 
    tale_title = models.CharField(max_length=50)
    tale_content = models.TextField()
    