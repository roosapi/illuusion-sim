from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

from tallit.models import Horse, Merit
import tallit.services as services

def horse(request, slug):
    horse = Horse.objects.select_related('sire', 'dam', 'breeder').get(address=slug)
    #print(slug, horse.name)
    offspring = []
    if horse.sex == 'ori':
        offspring = Horse.objects.filter(sire=horse.id)
    elif horse.sex == 'tamma':
        offspring = Horse.objects.filter(dam=horse.id)


    lines = {}
    vrl = services.get_vrl_info(horse.vh)
    
    merits = Merit.objects.filter(horse=horse.id)
    print(merits)

    horse.final_description = horse.description.replace(r'\n', '</p><p>')

    template = loader.get_template('hopeapaju/horse.html')
    context = {
        'horse': horse,
        'owner': horse.owner,
        'breeder': horse.breeder,
        'lineage': {'sire':horse.sire, 'dam':horse.dam},
        'vrl_info': vrl,
        'offspring': offspring,
        'merits': merits,
    }
    return HttpResponse(template.render(context, request))


def horses(request):
    horses = Horse.objects.filter(stable='Hopeapaju').order_by('breed', 'sex')
    template = loader.get_template('hopeapaju/horses.html')
    context = {
        'horses':horses.filter(status=0),
        'deceased':horses.filter(status=2),
        }
    return HttpResponse(template.render(context, request))

