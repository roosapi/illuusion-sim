import requests
from tallit.models import Horse, Merit

def get_vrl_info(vh):
    url = 'http://www.virtuaalihevoset.net/?rajapinta/ominaisuudet.html?' 
    params = {'vh': vh}
    r = requests.get(url, params=params)
    return r.json()

def check_horse_address(horse, stable):
    if horse.stable == stable:
        horse.address = '../'+horse.address
    return horse

def get_merit_string(horse):
    merits = Merit.objects.filter(horse=horse.id)
    m_s = []
    for m in merits:
        m_s.append(m.merit)
    return ' '.join(m_s)

def get_horse_pedigree(horse, gen_limit=6):
    maxgen = 0
    mingen = gen_limit
    def recurse(h, res, gen, prefix):
        nonlocal mingen
        nonlocal maxgen
        newgen = gen + 1
        if gen > gen_limit:
            maxgen = gen_limit
            return res
        if not h:
            h = {'prefix': prefix, 'horse': None}
            res.append(h)
            h['rowspan'] = 2**(gen_limit - gen)
            tempres = recurse(None, res, newgen, prefix + 'i')
            finres = recurse(None, tempres, newgen, prefix + 'e')         
            return finres   
        else:
            merits = get_merit_string(h)
            h = {'prefix': prefix, 'horse': check_horse_address(h, 'hopeapaju'), 'merits': merits}
            
            res.append(h)
            if h['horse'].evm and gen <= mingen:
                mingen = gen - 1
            h['rowspan'] = 2**(gen_limit - gen)
            tempres = recurse(h['horse'].sire, res, newgen, prefix + 'i')
            finres = recurse(h['horse'].dam, tempres, newgen, prefix + 'e')
            return finres

    return {
            'pedigree': recurse(horse.sire, [], 1, 'i') + recurse(horse.dam, [], 1, 'e'),
            'maxgen': maxgen,
            'mingen': mingen
           }

def get_horse_level(horse, disc):
    levels_krj = [
        ['Helppo D', 'Helppo C', 'KN Special', 'Helppo B', 'Helppo A'],
        ['Helppo C', 'KN Special', 'Helppo B'],
        ['Helppo A'], 
        ['Vaativa B'], 
        ['Helppo A'],
        ['Vaativa B'], 
        ['Vaativa A'], 
        ['Prix St. Georges'], 
        ['Intermediate I'], 
        ['Intermediate II'], 
        ['Grand Prix']
        ]
    levels_erj = [
        ['40cm','60cm','80cm','90cm','100cm'],
        ['80cm','90cm','100cm'],
        ['110cm'],
        ['120cm'],
        ['100cm', '130cm'],
        ['110cm', '140cm'],
        ['120cm'],
        ['130cm'],
        ['140cm'],
        ['150cm'],
        ['160cm'],
    ]
    levels_kerj = [
        ['Aloittelijaluokka', 'Harrasteluokka', 'Tutustumisluokka'],
        ['Aloittelijaluokka', 'Harrasteluokka', 'Tutustumisluokka'],
        ['Helppo'],
        ['CIC1'],
        ['CIC1'],
        ['CIC2'],
        ['CIC3'],
        ['CIC4'],
    ]
    if not horse.level:
        return ''
    max_levels = horse.level.split('|')
    vrl_info = get_vrl_info(horse.vh)
    if disc == 'koulu':
        vrl_level = vrl_info['krj']['level']
        if vrl_level < 0:
            vrl_level = 0
        lvls = levels_krj[vrl_level-1]
        if max_levels[0] in lvls:
            return max_levels[0]
        else:
            return lvls[len(lvls)-1]
    if disc == 'este':
        vrl_level = vrl_info['erj']['level']
        if vrl_level < 0:
            vrl_level = 0
        lvls = levels_erj[vrl_level-1]
        if max_levels[1] in lvls:
            return max_levels[1]
        else:
            return lvls[len(lvls)-1]
    if disc == 'kentta':
        vrl_level = vrl_info['kerj']['level']
        if vrl_level < 0:
            vrl_level = 0
        lvls = levels_kerj[vrl_level-1]
        if max_levels[2] in lvls:
            return max_levels[2]
        else:
            return lvls[len(lvls)-1]