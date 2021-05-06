 d = {'Alice': 45, 'Bob': 60, 'Candy': 75, 'David': 86, 'Ellena': 49 }
 if not d['Alice']:
     print("添加元素成功")
     d['Alice'] = 60
else:
     list = []
     list.append(d['Alice'])
     d['Alice'] = list
     list.append(60)
print(d)
