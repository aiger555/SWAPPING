from django.urls import path
from .views import BookAPIView, BookDetailAPIView

urlpatterns = [
    path('books/', BookAPIView.as_view(), name='book_list_url'),
    path('books/<int:id>/', BookDetailAPIView.as_view(), name='book_detail_url'),
]

