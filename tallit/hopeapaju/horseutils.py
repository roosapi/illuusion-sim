from tallit.models import Horse, Merit

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
                print('new mingen')
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