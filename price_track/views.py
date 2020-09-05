from django.shortcuts import render, HttpResponse
import webbrowser as web
import requests as r
from bs4 import BeautifulSoup as bs
import time

def index(request):
    return render(request, "index.html")
def price_tracker(request):
    flip = request.POST['flip']
    flip2 = int(request.POST['flip2'])
    flip2 = flip2
    a = flip
    indisale = a +'&affid=yogeshji28'
    b = r.get(a)
    b = b.content
    soup = bs(b, "html.parser")
    price = soup.find("div", {"class": "_3qQ9m1"}).text
    price = price[1:]
    price = int(price)
    if price < flip2:
        web.open(indisale)
    else:
        time.sleep(5)
    return render(request, "price.html", {"url": price, "url1": flip2})
