from django.shortcuts import render
from django.utils import timezone
from homepage.models import New, Idea
from homepage.forms import IdeaForm


def index(request):
    context = {
        'news_list': New.objects.order_by('date'),
        'ideas_list': Idea.objects.order_by('date'),
        'form': IdeaForm()
    }
    
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            
            challenge = None
            if form.cleaned_data['challenge'] != '':
                challenge = form.cleaned_data['challenge']
                
            idea = Idea(
                title = form.cleaned_data['title'],
                description = form.cleaned_data['description'],
                challenge = challenge,
                email = form.cleaned_data['email'],
                public = request.POST['type'] == 'public',
                date = timezone.now(),
                )   
            idea.save()
    
    return render(request, 'index.html', context)
