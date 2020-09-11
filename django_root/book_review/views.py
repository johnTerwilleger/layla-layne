from django.shortcuts import render
from models import BookReview


# Create your views here.
def single_review(request, book_review_id):
  # Get book review from database
  book_review = BookReview.objects.filter(id=book_review_id)
  # 

  return render(request, 'book_review/single_review', book_review)
