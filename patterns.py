import itertools
seq = ('access_time', 'role', 'company_id', 'field_id', 'url_pattern')
group_list = [];
for index, item in enumerate(seq):
    l = list(itertools.combinations(seq,index + 1))
    for index, item in enumerate(l):
        mojiretu = '&group_by[]='.join(item)
        print('group_by[]=' + mojiretu)
        group_list.append('group_by[]=' + mojiretu)

_seq = {'target_date' : '2018-01-29', 'user_id' : '9999', 'role' : '9', 'company_id' : '99', 'field_id' : '999', 'url' : 'home/dashboard'}
_keys = _seq.keys()
where_list = [];
for index in range(len(_keys)):
    l = list(itertools.combinations(_keys,index + 1))
    for index, item in enumerate(l):
        mojiretu = []
        for index, _item in enumerate(item):
            mojiretu.append(_item + '=' + _seq[_item])
        where_list.append('&'.join(mojiretu))

for group, where in itertools.product(group_list, where_list):
    print(group + '&' + where)
