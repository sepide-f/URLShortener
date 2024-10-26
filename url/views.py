import pyshorteners
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.utils import timezone
from django.contrib import messages
from .serializer import URLShortenerSerializer
from .models import URLShortener
from django.http import JsonResponse


class URLShortenerView(APIView):
    def post(self, request):
        url = request.data.get("url")
        if not url:
            return Response({"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST)
        shortener = pyshorteners.Shortener()
        short_code = shortener.tinyurl.short(url)
        data = {
            'url': url,
            'short_code': short_code,
            'created_at': timezone.now(),
            'updated_at': timezone.now(),
        }
        serializer = URLShortenerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, short_code):
        given_url = URLShortener.objects.filter(short_code=short_code)
        if not given_url:
            return JsonResponse({'error': 'url does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = URLShortenerSerializer(given_url)
        return JsonResponse(serializer.data, safe=False)

    def put(self, request, short_code):
        new_url = request.data.get("url")
        if not new_url:
            return Response({"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            given_url = URLShortener.objects.get(short_code=short_code)
        except URLShortener.DoesNotExist:
            return Response({'error': 'url does not exist'}, status=status.HTTP_404_NOT_FOUND)

        given_url.url = new_url
        given_url.updated_at = timezone.now()

        given_url.save()

        serializer = URLShortenerSerializer(given_url)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, short_code):
        try:
            given_url = URLShortener.objects.get(short_code=short_code)
        except URLShortener.DoesNotExist:
            return Response({'error': 'URL does not exist'}, status=status.HTTP_404_NOT_FOUND)

        given_url.delete()

        return Response({"message": "URL successfully deleted"}, status=status.HTTP_204_NO_CONTENT)



