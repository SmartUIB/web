from django.shortcuts import render
from django.utils import timezone
from homepage.models import Idea, Challenge
from homepage.forms import IdeaForm
from django.http import JsonResponse as json


def index(request):
    context = {
        'challenges': Challenge.objects.all()
    }
    
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            challenge, title = None, ""
            r_challenge, r_title = request.POST.get('challenge'), request.POST['title']
            if r_challenge:
                challenge = Challenge.objects.get(name=r_challenge)
            if r_title != '':
                title = r_title
                
            idea = Idea(
                title = title,
                description = form.cleaned_data['description'],
                challenge = challenge,
                email = form.cleaned_data['email'],
                public = request.POST.get('whose') == None,
                date = timezone.now(),
                )   
            idea.save()
            return json({'message': 'Thank you for your idea!'}, status=200)
            
        else:
            return json({'message': form.errors.as_text()}, status=500)
    
    return render(request, 'index.html', context)
