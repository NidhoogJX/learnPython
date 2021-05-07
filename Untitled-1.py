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
# def jttl(t:int,j:int): #鸡兔同笼求和函数
#      message ='鸡的数量:{}'.format(2*t-j/2)+'兔的数量:{}'.format(j/2-t)
#      return message
# print(jttl(35,96))

# def sum(num): #求和函数
#      i = 0
#      j = 0
#      if not isinstance(num,int):
#           message = "输入的值不正确，请输入数值类型"
#           return message
#      while i <= num:
#           j = j + i
#           i += 1 
#      return j
# print(sum(100))


# def dg(num):
#      if num == 1:
#           return 1
#      else:
#           return num +dg(num-1) 
# print(dg(100))

# def print_test(str1,str2="world"):
#      if not isinstance(str1,str):
#           return '输入的值不正确。请输入字符'
#      else:
#           if not str1:
#                return 'hello,{}'.format(str2)
#           else:
#                return 'hello,{}'.format(str1)
# print(print_test('NidhoogJX'))

# def average(*args): 
#      sum = 0 
#      for item in args: 
#           sum += item 
#           avg = sum / len(args) 
#           return avg
# print(average(1,2,3,4,5))
# def info(**kwargs): 
#      names = kwargs['names'] 
#      gender_list = kwargs['gender'] 
#      age_list = kwargs['age'] 
#      index = 0 
#      for name in names: 
#           gender = gender_list[index] 
#           age = age_list[index] 
#           print('name: {}, gender: {}, age: {}'.format(name, gender, age)) 
#           index += 1 
# info(names = ['Alice', 'Bob', 'Candy'], gender = ['girl', 'boy', 'girl'], age = [16, 17, 15])
