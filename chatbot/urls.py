from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot_html_view, name='chatbot'),  # Render HTML for chatbot and handle form submission
]