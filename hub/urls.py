from django.urls import path

from hub.views import index, SwaggerUIView

urlpatterns = [
    path('', index, name='index'),
    path('swagger/', SwaggerUIView.as_view()),
]