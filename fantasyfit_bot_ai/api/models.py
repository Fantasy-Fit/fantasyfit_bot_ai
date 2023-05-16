from django.db import models

class BotComment(models.Model):
    input_prompt = models.CharField(max_length=500)
    gpt_response = models.CharField(max_length=2000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.input_prompt
