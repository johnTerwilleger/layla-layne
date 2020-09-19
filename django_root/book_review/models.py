import uuid
import datetime
from django.db import models


# Create your models here.
class BookReview(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  title = models.TextField()
  author = models.TextField()
  review = models.TextField()
  summary = models.TextField()
  genre = models.IntegerField()
  rating = models.IntegerField()
  date_entered = models.DateField()
  tags = models.TextField()

  def __init__(self,
    title='',
    author='',
    review='',
    summary='',
    genre=0,
    rating=0,
    date_entered=datetime.datetime.today(),
    tags=''):
    self.title = title
    self.author = author
    self.review = review
    self.summary = summary
    self.genre = genre
    self.rating = rating
    self.date_entered = date_entered
    self.tags = tags
    
    
  def __str__(self):
    return self.title


  def add():
    self.save()

  