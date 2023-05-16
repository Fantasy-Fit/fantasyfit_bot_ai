from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import BotCommentSerializer
from api.models import BotComment
from django.http import JsonResponse

from django.shortcuts import render, HttpResponse

import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = str(os.getenv("OPENAI_KEY"))

def Index(request):
    return HttpResponse("FFit Django Server is Running!")


class BotCommentAV(APIView):
    
    def post(self, request):
        input_prompt = "Adopting the tone of a fitness coach with a sarcastic but forceful and serious tone, write several sentences based on the history of user workouts who are participants in a fitness competition where workouts generate points to provide some encouragement, banter and throw some shame at who's being lazy. If there are no workouts, adopt a midly angry tone to encourage participants to start working out." 
        msg_list = request.data.get('prompts', [])
        msg_list.append({"role": "user", "content": input_prompt})
        
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = msg_list
        )
        
        gpt_response = response["choices"][0]["message"]["content"]
        msg_list.append({"role": "assistant", "content": gpt_response})
        
        data = {
            "input_prompt": input_prompt,
            "gpt_response": msg_list[-1]['content']
        }
    
        serializer = BotCommentSerializer(data=data)
        print("line 39", serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
        
        
