# print ("hello world")

# #演算
# print (10 % 3)
# print (15 / 3)

#変数
# string = 'hello'
# string_times = 5.5
# string_length = 5

# print(string)

# #条件分岐

# if string == 'hello world':
#   print("nice to meet you")
# elif string == 'hello':
#   print ('Hi')
# else:
#   print('wow')

# #関数
def country_num(arg):
  countries = arg

  if (countries < 10):
    return 'sukunai'
  else:
    return 'ooi'

# print(country_num(4))

# list
# countries =['japan', 'korea', 'chine']
# print(countries[0])

#for

# for index in range(3):
#   print (country_num(index))

# for item in countries:
#   print(item)

#with
#open

# with open('./test.text', 'r') as file:
#   print(file.read())


#class
# class Card:
#   def __init__(self,date,user_name):
#     self.date = date
#     self.user_name = user_name
#   def message(self):
#     return 'この投稿は' + self.user_name + 'さんが' + self.date + 'に投稿しました'
# date_a = '2020-01-01'
# user_name_a = 'taro'
# card_a = Card(date_a, user_name_a)

# date_b = '2020-01-03'
# user_name_b = 'yoko'
# card_b = Card(date_b, user_name_b)

# print(card_b.message())

#import
# import math
# print(math.pi)
#例　Flask Django等

# import numpy

# numpy_list =[3,1,5,2093,10]

# print (numpy,sum(numpy_list))