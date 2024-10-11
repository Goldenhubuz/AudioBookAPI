from django.contrib import admin

from apps.base.admin import BaseAdmin
from apps.book.models import Book, BookReview, LatestSearch


class BookAdmin(BaseAdmin):
    # list_display = [f.name for f in Book._meta.fields]
    list_display = ['id', 'title', 'author', 'rate', 'pages_count']
    save_as = True


admin.site.register(Book, BookAdmin)

class BookReviewAdmin(BaseAdmin):
    list_display = [f.name for f in BookReview._meta.fields]

class LatestSearchAdmin(BaseAdmin):
    list_display = [f.name for f in LatestSearch._meta.fields]


admin.site.register(BookReview, BookReviewAdmin)
admin.site.register(LatestSearch, LatestSearchAdmin)
