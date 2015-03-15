from django.shortcuts import render
from django.http import HttpResponse

import requests

def index(request):
    apiKey = 'm776710682-a0e34d5943f5727e485c1627'

    request = {
        'apiKey': apiKey,
        'monitors': 776710682,
        'logs': 1,
        'format': 'json',
        'noJsonCallback': 1
    }
    r = requests.get('https://api.uptimerobot.com/getMonitors', params=request)
    data = r.json()

    return HttpResponse(data.get('monitors')['monitor'][0]['status'])
