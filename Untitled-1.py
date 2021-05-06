#  d = {'Alice': 45, 'Bob': 60, 'Candy': 75, 'David': 86, 'Ellena': 49 }
#  if not d['Alice']:
#      print("添加元素成功")
#      d['Alice'] = 60
# else:
#      list = []
#      list.append(d['Alice'])
#      d['Alice'] = list
#      list.append(60)
# print(d)
# d = {'Alice': 45, 'Bob': 60, 'Candy': 75, 'David': 86, 'Ellena': 49 }
# d.pop('Alice')
# print(d)
# key = (1, 2, 3) # 以tuple作为key 
# d[key] = True
# print(d)
# for key,value in d.items(): 
#      print(value)
# print(len(d.items()))
# set_name = set([1, 4, 3, 2, 5, 4, 2, 3, 1])
# print(set_name)
def jttl(t:int,j:int):
     message ='鸡的数量:'+str(round((2*t-j/2),0)) +'兔的数量:'+str(round((j/2-t),0))
     return message
print(jttl(35,96))
