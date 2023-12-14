from django.urls import path
from .views import BookListAPIView, BookCreateAPIView, BookRetrieveAPIView, BookDestroyAPIView, BookRetrieveUpdateAPIView

urlpatterns = [
    path('', BookListAPIView.as_view(), name='book_list'),
    path('add/', BookCreateAPIView.as_view(), name='book_add'),
    path('<int:pk>/', BookRetrieveAPIView.as_view(), name='book_detail'),
    path('delete/<int:pk>/', BookDestroyAPIView.as_view(), name='book_delete'),
    path('update/<int:pk>/', BookRetrieveUpdateAPIView.as_view(), name='book_update'),
]
