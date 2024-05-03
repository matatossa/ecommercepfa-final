from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import chat  # Import your chatbot logic


@csrf_exempt
def chatbot_view(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user_input = data.get('user_input', '')  # Get user input from the JSON data
        # Process user input using your chatbot logic
        bot_response = process_input(user_input)  # Replace with your actual chatbot logic
        return JsonResponse({'bot_response': bot_response})
    else:
        return JsonResponse({'error': 'Unsupported method'}, status=400)
from django.shortcuts import render
from django.http import JsonResponse
from . import chat  # Import your chatbot logic

def chatbot_html_view(request):
    bot_response = None
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        bot_response = chat.process_input(user_input)  # Replace with your actual chatbot logic

    return render(request, 'shop/chatbot/chatbot.html', {'bot_response': bot_response})
