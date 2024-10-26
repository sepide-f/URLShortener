from django.urls import path
from .views import URLShortenerView

urlpatterns = [
    path("shorten/", URLShortenerView.as_view(), name='shortener'),
    path("shorten/<str:short_code>/", URLShortenerView.as_view(), name='shortener'),
    path("put/shorten/<str:short_code>/", URLShortenerView.as_view(), name="shortener"),
    path("delete/shorten/<str:short_code>/", URLShortenerView.as_view(), name="shortener"),
]

