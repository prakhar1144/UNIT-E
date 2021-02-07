from django.shortcuts import render
import requests
from .models import Mess,Event
from django.utils import timezone
import requests
from bs4 import BeautifulSoup 

# Create your views here.

def home(request):
    posts = Event.objects.filter()[::-1]
    if request.user.is_authenticated:
        return render(request, "baseapp/mainpg.html")
    else:
        return render(request, "baseapp/home.html", {'posts':posts})

def result(request, email):
    user_roll = int(email[0:6])
    print(user_roll)
    url = "https://nithp.herokuapp.com/api/result/student/{roll}"
    data = requests.get(url.format(roll=user_roll)).json()
    dictionary = {}
    for res in data['result']:
        if res['sem'] not in dictionary:
            dictionary[res['sem']] = []
        dictionary[res['sem']].append([res['grade'],res['sub_gp'],res['sub_point'],res['subject'],res['subject_code']])
    i=1
    for summ in data['summary']:
        print(summ)
        dictionary[i].append(summ)
        i += 1 
    return render(request, "baseapp/result.html", {'data':dictionary})

def mess(request, email):
    roll_first_two = int(email[0:2])
    mess_data = Mess.objects.get(roll_starts_with=roll_first_two)
    return render(request, 'baseapp/mess.html', {'mess_data':mess_data})

def newsfeed(request):
    posts = Event.objects.filter()[::-1]
    return render(request, 'baseapp/newsfeed.html', {'posts':posts})

def notice(request):
    url = "https://nith.ac.in/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    announcement = soup.find(id="Announcements")  #annoucement represents a div having id="Announcement"
    links = announcement.find_all('a')  #links represents
    LINKS = []
    for link in links:
        LINKS.append([link.text,link.get('href')])
    print(LINKS)
    return render(request, 'baseapp/notice.html', {'LINKS': LINKS})

def contributor(request):
    return render(request, 'baseapp/contributor.html')