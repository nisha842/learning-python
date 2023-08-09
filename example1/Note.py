#list
fruits=['orange', 'banana','kiwi','grapes']
print(fruits[1:2]) #slice

#accessing elements
print(fruits[2])
#mutable assignment
fruits[0]='guava'
print(fruits)
fruits.append('strawberry')
print(fruits)
fruits.insert(2,'nisha') #insert with position
print(fruits)
numbers=[1,2,4,5,6,7]
print(len(numbers)) #length
squared_numbers=[x**2 for x in numbers]
print(squared_numbers)

#dictionary

my_profile={'name':'nisha','age':28,'profession':'pharmacist'}
print(my_profile['profession']) #accessing values

my_profile['age']=20  #change
print(my_profile)

values=[1,2,3,4,5]  #dict comprehension
squared_dict={x:x**2 for x in values}
print(squared_dict)

#nested structure

class method#Constructor method that initializes the object's attributes when an instance is created.
class player:
    def __init__(self,name):
        self.name=name
        self.position= None

    def set_position(self,position):
        self.position=position



