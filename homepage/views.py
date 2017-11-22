from django.shortcuts import render
from django.utils import timezone
from homepage.models import New, Idea


def index(request):
    context = {
        'news_list': New.objects.order_by('date'),
        'ideas_list': Idea.objects.order_by('date'),
    }
    
    return render(request, 'index.html', context)
