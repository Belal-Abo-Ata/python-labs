from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Book , Isbn

@receiver(pre_save, sender=Book)
def create_and_assign_isbn(sender, instance, **kwargs):
    if not instance.isbn_id:
        isbn = Isbn.objects.create(
            author_title='Default Author',
            book_title=instance.title
        )
        instance.isbn = isbn



