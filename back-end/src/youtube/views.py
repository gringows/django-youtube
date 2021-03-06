from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.

def index(request):

    context = {}
    videos = Video.objects.all()
    context['videos'] = videos  
    return render(request, 'youtube/index.html', context)

def new_video(request):

    context = {}

    if request.method == 'POST':
        form = NewVideo_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = NewVideo_Form()
    context['form'] = form
    return render(request, 'youtube/new_video.html', context)

def video(request, pk):

    
    video = Video.objects.get(pk=pk)
    comments = Comment.objects.filter(video=video)

    if request.method == 'POST':
        form = Coment_Form(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user.username
            comment.video = video
            comment.save()
    else:
        form = Coment_Form()
    
    context = {
        'video' : video,
        'form' : form,
        'comments' : comments,
    }

    return render(request, 'youtube/video.html', context)