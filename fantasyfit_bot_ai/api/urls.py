from django.urls import path
from .views import BotCommentAV

urlpatterns = [
    path('botcomment/', BotCommentAV.as_view(), name="bot-comment"),
]