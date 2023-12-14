from django.db import models

class Book(models.Model):
    '''Model representing books.'''
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    genre = genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title
