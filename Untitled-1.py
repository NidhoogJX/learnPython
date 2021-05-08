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
# class Animal(object): 
#     __count = 0 
#     def __init__(self): 
#         Animal.__count += 1
#         print(Animal.__count)
# dog = Animal()
# cat = Animal()
# class Anmail(object): pass 
# dog = Anmail() 
# cat = Anmail()
# print(dog)
# print(cat)
# dog.name = 'dog'
# dog.age = 5
# cat.name = 'dog'
# cat.age = 5
# class Animal(object): 
#     def __init__(self, name, age): 
#         self.name = name 
#         self.__age = age 
# cat = Animal('Kitty', '3') 
# print(cat.name) 
# print(cat.__age)
# class Animal(object): 
#     __shape = "big"
#     def __init__(self, name="NifhoogJX", age=10, localtion="china"): 
#         self.__name = name 
#         self.__age = age 
#         self.__localtion = localtion 
#     def set_shape(self, shape): 
#         Animal.__shape = shape
#     def update_info(self, name, age, localtion): 
#         self.__name = name 
#         self.__age = age 
#         self.__localtion = localtion
#     def get_info(self): 
#         return 'name = {}, age = {}, localtion = {}'.format(self.__name, self.__age, self.__localtion) 
#     def get_shape(self):
#         return Animal.__shape
# JX = Animal()
# print(JX.get_info())
# JX.update_info("jx",22,"suzhou")
# print(JX.get_info())
# JX.set_shape("small")
# print(JX.get_shape())
# dog = Animal('wangwang', 1, 'GuangDong')
# class Person(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
# class Teacher(Person):
#         def __init__(self, name, gender, course):
#             super(Teacher,self).__init__(name,gender)
#             self.course = course
# teacher = Teacher('Alice', 'Female', 'English')
# print(teacher.name)
# print(teacher.gender)
# print(isinstance(teacher,object))
# print(dir(teacher))
# print(dict(teacher))


class Person(object): 
    pass 
class Student(Person): 
    pass 
class Teacher(Person): 
    pass 
class SkillMixin(object): 
    pass 
class BasketballMixin(SkillMixin): 
    def skill(self): 
        return 'basketball' 
class FootballMixin(SkillMixin): 
    def skill(self): 
        return 'football' 
class BStudent(BasketballMixin, Student): 
    pass 
class FTeacher(FootballMixin, Teacher): 
    pass 
s = BStudent() 
print(s.skill()) 
t = FTeacher() 
print(t.skill())
class Person(object): 
    def __init__(self, name, gender, **kw): 
        self.name = name 
        self.gender = gender 
        for k, v in kw.items(): 
            setattr(self, k, v) 
p = Person('Bob', 'Male', age=18, course='Python') 
print(p.age) 
print(p.course)


