from django.shortcuts import render
from youtube_transcript_api import YouTubeTranscriptApi

# Create your views here.


def home(request):
    return render(request, 'home.html')


def pro(request):
    # name = request.GET['code']
    hint = request.GET['hint']
    links = request.GET['links']
    name = request.GET['links'].split("=")[1]
    links = links.replace('watch?v=', 'embed/')
    print(name)
    data = YouTubeTranscriptApi.get_transcript(name)
    subtitles = {}
    for i in data:
        if hint in i['text']:
            subtitles[round(i['start'])] = i['text']
    print(subtitles)
    return render(request, 'second.html', {'subtitles': subtitles, 'link': links})


def jump(request):
    tf = request.GET['timeframe']
    print(tf)
    return render(request, 'home.html')
