log = """name:Иван;gender:m;item:Часы;item_cost:9800
name:Иван;gender:m;item:Фитнес-браслет;item_cost:12300
name:Иван;gender:m;item:Кофемашина;item_cost:23500
name:Петр;gender:m;item:Часы;item_cost:9800
name:Петр;gender:m;item:Фитнес-браслет;item_cost:12300
name:Петр;gender:m;item:Айфон;item_cost:77900
name:Петр;gender:m;item:Чехол для телефона;item_cost:350
name:Петр;gender:m;item:Кофемашина;item_cost:23500
name:Дарья;gender:m;item:Айфон;item_cost:77900
name:Марья;gender:m;item:Кофемашина;item_cost:23500
name:Юлия;gender:m;item:Фитнес-браслет;item_cost:12300"""
 
# for info in log.split('\n'):
#     data = info.split(':')[3:]
#     price = int(data.pop(-1))
#     merchandise = ''.join(data).split(';')[0]
#     if price < 20000:
#         print(merchandise, price)

for info in log.split('\n'):
     data = info.split(':')[3:]
     price = int(data.pop(-1))
     merchandise = ''.join(data).split(';')[0]
     if price < 13000:
          print(merchandise, price)