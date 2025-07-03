from django.db import models

class Collection(models.Model):
    collection_name=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    collcover=models.CharField(max_length=1000)

    def __str__(self):
        return self.collection_name

class Piece(models.Model):
    title=models.CharField(max_length=200)
    typ=models.CharField(max_length=200)
    artist=models.CharField(max_length=200)
    year = models.IntegerField(default=2000)
    piececover=models.CharField(max_length=1000)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name="pieces")

    def __str__(self):
        return self.title
    
# 🔥 New Model
class Story(models.Model):
    piece = models.ForeignKey(Piece, on_delete=models.CASCADE, related_name='stories')
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return f"{self.title} ({self.piece.title})"