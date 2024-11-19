from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# "/" uchun funksiya
def home(request):
    return render(request, 'advertisement/home.html')

# "/users/" uchun funksiya
def users(request):
    user_list = ["Ali", "Vali", "Salim", "Nodir", "Aziz"]
    return JsonResponse({"users": user_list})

# "/ads/" uchun funksiya
def ads(request):
    # Chiroyli HTML reklama uchun
    return render(request, 'advertisement/ads.html')