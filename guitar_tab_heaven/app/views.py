from django.shortcuts import render
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def tab_detail_view(request, url):
    tab_url = "http://www.guitartabs.cc/" + url
    tab_result = requests.get(tab_url).text
    souper = BeautifulSoup(tab_result, "html.parser")
    tab = str(souper.find_all("pre"))
    stripped_tab = tab.strip("[]")

    return render(request, "detail.html", {"tab": tab, "stripped_tab": stripped_tab})

def tab_search_view(request):
    song_name = request.GET.get("song") or "Smells Like Teen Spirit"
    url = "http://www.guitartabs.cc/search.php?tabtype=any&band=&song={}".format(song_name)
    results = requests.get(url).text
    souper = BeautifulSoup(results, "html.parser")
    links = [link["href"] for link in souper.find_all("a", class_="ryzh22")]
    paging = souper.find_all(class_="paging")
    # print(results)

    return render(request, "index.html", {"links": links, "paging": paging})
