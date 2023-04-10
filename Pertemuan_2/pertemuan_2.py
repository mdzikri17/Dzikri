
#thislist = ["apple","banana","orange","kiwi","melon", "mango"]
#print(thislist[2:5])
#thislist = ["apple","banana","orange","kiwi","melon", "mango"]
#print(thislist[:4])
#thislist = ["apple","banana","orange","kiwi","melon", "mango"]
#print(thislist[2:])
#thislist = ["apple","banana","orange","kiwi","melon", "mango"]
#print(thislist[-1:-4])

#thislist = ["apple","banana","orange","kiwi", "mango"]
#thislist[1:3] = ["blackcurrent", "watermelon"]
#print(thislist)

#thislist = ["apple","banana","orange"]
#thislist[1:2] = ["blackcurrent", "watermelon"]
#print(thislist)

#thislist = ["apple", "banana", "cherry"]
#thislist.insert(0, "orange")
#print(thislist)

#thislist = ["apple","banana"]
#thislist.remove("apple")
#thislist.pop(0)
#print(thislist)

#thislist = ["apple","banana"]
#thislist.clear()
#print(thislist)

#fruits = ["apple", "banana", "cherry"]
#for x in fruits:
 # print(x)

#fruits = ["apple", "banana", "cherry"]
#for x in fruits:
  #print(x)
  #if x == "banana":
    #break

#thislist = ["apple","banana","mango"]
#[print(x) for x in [thislist]]

thislist = ['apple','banana','mango']

thislist.remove('banana')
assert(thislist) == ['apple', 'mango']

thislist.append('kiwi')
assert(thislist) == ['apple','mango','kiwi']


#new_list = ['apple', 'apple', 'apple' 'apple', 
            #'mango', 'kiwi', 'apple', 'apple', 
           #'apple', 'apple']

#assert(new_list[4:6]) == ['mango', 'kiwi']

#new_list = ['apple', 'apple', 'apple' 'apple', 
            #'mango', 'kiwi', 'apple', 'apple', 
            #'mango','kiwi'
            #'apple', 'apple']
#assert([x for x in new_list if x != 'apple']) == ['mango', 'kiwi','mango', 'kiwi']

#list1 = ['mango']
#list2 = ['apple']

#list1 += list2
#list1.sort(reverse=True)
#print(list1)

#list1 = [1,4,5,6,2,4]
#list1.reverse()
#print(list1)

#list1 = [1,4,5,6,2,4]
#assert([x for x in list1 if x != 4]) == [1,5,6,2]

#assert([x for x in list1 if x == 4]) == [4,4]

#list1 = [1,4,5,6,2,4]
#list2 = list1.copy()
#list2.pop()

#print(list1,list2)

#list1 = [1,4,5,7]

#list3 = list2.copy

#assert(list3) == [1,4,5]
#assert(list1) == list1

#fruits = ("apple", "banana", "cherry")

#(green, yellow, red) = fruits

#print(green)
#print(yellow)
#print(red)

#cars = {
    #'brand': 'honda',
    #'product': 'civic'
#}

#print(cars['brand'])
#print(cars['key'])

#cars = {
    #'brand':'honda'
    #'products'  'civic'
#}

#assert (list(cars.keys()[1])) == 'products'

#rint(cars.values)

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def full_name(first_name, last_name):
  print(first_name+" "+last_name)

full_name(last_name="Tobias", first_name="Emil")

def multiply_by_two(a):
    return(a * 2)
assert(multiply_by_two(3)) == 6

def multiply_by_x(b,c = 2):
   return b * c

assert(multiply_by_x(3)) == 6
assert(multiply_by_x(3, 1)) == 3

user_input = input('input di kali 2: ')
print(multiply_by_two(int(user_input)))

how_many_input = input("berapa kali ingin input")
i = 0
while i < int(how_many_input):
   user_input = input('input dikali dua')
   print(multiply_by_two(int(user_input)))

how_many_input = input('berapa kali input')
i=0
while True:
    if i == 0:
       break

    user_input = input('input dikali dengan 2 ')
    print(multiply_by_two(int(user_input)))
    i += 1