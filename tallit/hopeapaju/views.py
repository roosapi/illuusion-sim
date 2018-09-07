from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

from tallit.models import Horse, Merit
from . import horseutils
import tallit.services as services

def index(request):
    template = loader.get_template('hopeapaju/index.html')
    return HttpResponse(template.render({}, request))

def horse(request, slug):
    horse = Horse.objects.select_related('sire', 'dam', 'breeder').get(address=slug)
    offspring = []
    if horse.sex == 'ori':
        offspring = Horse.objects.filter(sire=horse.id)
    elif horse.sex == 'tamma':
        offspring = Horse.objects.filter(dam=horse.id)

    for foal in offspring:
        foal = horseutils.check_horse_address(foal, 'hopeapaju')
         
    maxgen = 3
    if int(horse.pedigree) < 3:
        maxgen = 2
    lines = horseutils.get_horse_pedigree(horse, maxgen)
    vrl = services.get_vrl_info(horse.vh)
    
    merits = Merit.objects.filter(horse=horse.id)
    horse.final_description = horse.description.replace(r'\n', '</p><p>')

    template = loader.get_template('hopeapaju/horse.html')
    context = {
        'horse': horse,
        'owner': horse.owner,
        'breeder': horse.breeder,
        'lineage': lines,
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

