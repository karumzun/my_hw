GeekTech = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}
del GeekTech['bag']
GeekTech['address'] = 'Ibraimova 103'
GeekTech['number'] = '+996 507-05-20-18'
GeekTech['instagram'] = '@geektech_kg'
GeekTech['courses'].append('IOS')
GeekTech['courses'].append('UX/UI')
GeekTech['courses'] = set(GeekTech['courses'])
for k, v in GeekTech.items():
    print(f'{k}: {v}')
