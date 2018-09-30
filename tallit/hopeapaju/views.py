from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
# Create your views here.

from tallit.models import Horse, Merit, Competition, Show, HorseImg, HorseText
from . import horseutils
import tallit.services as services

def index(request):
    template = loader.get_template('hopeapaju/index.html')
    return HttpResponse(template.render({}, request))

def pv(request):
    horses = Horse.objects.select_related('sire', 'dam').filter(breeder=22).order_by('-dob')
    context = {
        'hann': horses.filter(breed='hannover'),
        'hols': horses.filter(breed='holstein')
        }
    template = loader.get_template('hopeapaju/pv.html')
    return HttpResponse(template.render(context, request))

def sh(request):
    horses = Horse.objects.select_related('sire', 'dam').filter(breeder=22).order_by('-dob')
    context = {
        'horses': horses.filter(breed='suomenhevonen'),
        }
    template = loader.get_template('hopeapaju/sh.html')
    return HttpResponse(template.render(context, request))

def horselist(request, breed):
    breeds = ['hannover', 'holstein', 'suomenhevonen']
    if breed not in breeds:
        return HttpResponseNotFound()

    horses = Horse.objects.select_related('sire', 'dam').filter(stable='Hopeapaju', breed=breed).order_by('pedigree','dob')
    template = loader.get_template('hopeapaju/horselist.html')

    if breed == 'suomenhevonen':
        base_template = "hopeapaju/sh_base.html"
    else:
        base_template =  "hopeapaju/pv_base.html"

    context = {
        'base_template': base_template,
        'breed': breed,
        'stallions': horses.filter(status=0,sex='ori'),
        'mares': horses.filter(status=0,sex='tamma'),
        'deceased':horses.filter(status=2)
        }
    return HttpResponse(template.render(context, request))

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
    vrl = {}
    if horse.vh:
        vrl = horseutils.get_vrl_info(horse.vh)
    merits = Merit.objects.filter(horse=horse.id)
    horse.final_description = horse.description.replace(r'\n', '</p><p>')
    horse.current_level = horseutils.get_horse_level(horse, horse.discipline)
    competitions = Competition.objects.filter(horse=horse.id).order_by('discipline', 'date')
    shows = Show.objects.filter(horse=horse.id).order_by('type', 'date')
    texts = HorseText.objects.filter(horse=horse.id).order_by('-date')
    for text in texts:
        text.text = text.text.replace(r'\n', '</p><p>')
    images = HorseImg.objects.select_related('copy').filter(horse=horse.id)

    template = loader.get_template('hopeapaju/horse.html')
    context = {
        'horse': horse,
        'owner': horse.owner,
        'breeder': horse.breeder,
        'lineage': lines,
        'vrl_info': vrl,
        'offspring': offspring,
        'merits': merits,
        'competitions': competitions,
        'shows': shows,
        'images': images,
        'texts': texts,
    }
    return HttpResponse(template.render(context, request))


def horses(request):
    horses = Horse.objects.filter(stable='Hopeapaju').order_by('breed','sex','pedigree','dob')
    template = loader.get_template('hopeapaju/horses.html')
    context = {
        'horses': [
            {'title':'Hannover', 'horses':horses.filter(status=0,breed='hannover')},
            {'title':'Holstein', 'horses':horses.filter(status=0,breed='holstein')},
            { 'title':'Suomenhevonen', 'horses':horses.filter(status=0,breed='suomenhevonen')},
            {'title':'Myynnissä', 'horses':horses.filter(status=1)}
            ],
        'deceased':horses.filter(status=2),
        }
    return HttpResponse(template.render(context, request))

