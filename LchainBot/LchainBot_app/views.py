from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import os
from .bot import bot_instance
import logging
logger = logging.getLogger('django')
logger.info('Logger Check')


def index(request):
    print("hello")
    return render(request, 'index.html')

def get_response(request):
    if request.method == "POST":
        user_message = request.POST.get('message')
        response_message = bot_instance.get_response(user_message)
        print(response_message)
        return JsonResponse({'response': response_message['answer']})
        #return HttpResponse(response_message['answer'])
    return JsonResponse({'response': 'Invalid request'}, status=400)


