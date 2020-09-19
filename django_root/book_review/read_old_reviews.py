from models import BookReview


f = open('D:\Projects\lyla-layne\old_data\book_reviews.txt', 'r')
review = BookReview()
lines = f.readlines()
count = 0
for line in lines:
  #if it is the start of a book review
  if line.trim() == 'start':
    review.review = review_text
    print(review)
    #review.save()
    review = BookReview()
    count = 0
    review_text = ''
    continue
  
  elif count == 0:
    review.title = line.split('"')[1].trim()
    review.author = line.split('By:')[1].trim()

  elif count == 1:
    review.date_entered = line
  
  elif count == 5:
    review.rating = line.count('*')

  elif count == 7:
    review.genre = line.split('GENRE:')[1].trim()

  elif count == 8:
    review.summary = line

  elif count > 9:
    #Create the review string here
    review.review = review.review + '\n' + line




  count = count + 1









