from rest_framework import serializers
from api.models import BotComment

class BotCommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BotComment
        fields = "__all__"