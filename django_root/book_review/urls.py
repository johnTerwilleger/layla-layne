from django.urls import path
import views

urlpatterns = [
  path('book_review/<int:review_id>/', views.book_review_id)


]
