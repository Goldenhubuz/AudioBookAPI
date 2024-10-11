from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter

from apps.book.views import BookViewSet, BookReviewViewSet

# Root router for books
router = DefaultRouter()
router.register(r'', BookViewSet, basename='books')  # This handles /books/

# Nested router for BookReviews related to a specific book
book_reviews_router = NestedSimpleRouter(router, r'', lookup='book')
book_reviews_router.register(r'reviews', BookReviewViewSet, basename='book-reviews')

# Combine all routes
urlpatterns = router.urls + book_reviews_router.urls
