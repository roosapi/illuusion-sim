from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

from tallit.models import Horse, Merit
import tallit.services as services

def index(request):
    template = loader.get_template('hopeapaju/index.html')
    return HttpResponse(template.render({}, request))

def check_horse_address(horse, stable):
    if horse.stable == stable:
        horse.address = '../'+horse.address
    return horse

def get_horse_pedigree(horse, gen_limit=6):
    maxgen = 0
    mingen = gen_limit
    def recurse(h, res, gen, prefix):
        nonlocal mingen
        nonlocal maxgen
        if gen > gen_limit:
            maxgen = gen_limit
            return res
        if not h:
            if gen < mingen:
                mingen = gen
            elif gen > maxgen:
                maxgen = gen
            return res
        else:
            h = {'prefix': prefix, 'horse': check_horse_address(h, 'hopeapaju')}
            res.append(h)
            newgen = gen
            if not h['horse'].evm:
                newgen = gen + 1
            h['rowspan'] = 2**(gen_limit - gen)
            tempres = recurse(h['horse'].sire, res, newgen, prefix + 'i')
            finres = recurse(h['horse'].dam, tempres, newgen, prefix + 'e')
            return finres

    return {
            'pedigree': recurse(horse.sire, [], 1, 'i') + recurse(horse.dam, [], 1, 'e'),
            'maxgen': maxgen,
            'mingen': mingen
           }


def horse(request, slug):
    horse = Horse.objects.select_related('sire', 'dam', 'breeder').get(address=slug)
    #print(slug, horse.name)
    offspring = []
    if horse.sex == 'ori':
        offspring = Horse.objects.filter(sire=horse.id)
    elif horse.sex == 'tamma':
        offspring = Horse.objects.filter(dam=horse.id)

    for foal in offspring:
        foal = check_horse_address(foal, 'hopeapaju')
        
    sire = horse.sire#check_horse_address(horse.sire, 'hopeapaju')

    dam = horse.dam#check_horse_address(horse.dam, 'hopeapaju')
    
    lines = get_horse_pedigree(horse, 3)
    print(lines)
    vrl = services.get_vrl_info(horse.vh)
    
    merits = Merit.objects.filter(horse=horse.id)
    horse.final_description = horse.description.replace(r'\n', '</p><p>')

    template = loader.get_template('hopeapaju/horse.html')
    context = {
        'horse': horse,
        'owner': horse.owner,
        'breeder': horse.breeder,
        'lineage': {'sire':sire, 'dam':dam, 'lines':lines},
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

