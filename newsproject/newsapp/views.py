from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    r=requests.get('https://newsapi.org/v2/everything?q=everything&language=en&from=2022-06-23&sortBy=popularity&apiKey=84c58d88247849c7827e5d4c4068b03a')
    res=r.json()
    data=res["articles"]
    title=[]
    description=[]
    image=[]
    url=[]
    for i in data:
        title.append(i["title"])
        description.append(i["description"])
        image.append(i["urlToImage"])
        url.append(i["url"])
    news=zip(title,description,image,url)
    return render(request,"newsapp/index.html",{"news":news})

def search(request):
    r=requests.get('https://newsapi.org/v2/everything?q=everything&language=en&from=2022-06-23&sortBy=popularity&apiKey=84c58d88247849c7827e5d4c4068b03a')
    res=r.json()
    data=res["articles"]
    title=[]
    description=[]
    image=[]
    url=[]
    for i in data:
        title.append(i["title"])
        description.append(i["description"])
        image.append(i["urlToImage"])
        url.append(i["url"])
    news=zip(title,description,image,url)

    return render(request, "newsapp/index.html", {"news": news})

    search_term=""
    if search_term in news:
        return render (request, 'newsapp/index.html', {'news' : news, 'search_term': search_term })