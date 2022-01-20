```
class NameOfClass():

    def __init__(self,param1,param2):
        self.param1 = param1
        self.param2 = param2
    
    ## self - method is connected to the instance of the class
    def other_method(self):
         print(self.param1)    
```

myset = set()  
mylist = [1,2,3]  

### Class with Instance Attributes ( self ) 

```
class Dog():
    def __init__(self,mybreed)
        self.breed = mybreed
````

my_dog = Dog(mybreed='Huskie')  

### Class Object attribute - same for any instance [ NO self ]   

```
class Dog():
    species = 'mammal'
    def __init__(self,mybreed)
        self.breed = mybreed
````

### Instance menthods

```
def method(self):
    print(f'Instance attribute {self.breed}')
```

### Inheritance 
```
clss Animal():
    def __init__(self):
        print("Animal Created")
    def who_am_i(self):
        print("I am an animal")
    def eat(self):
        print("Eating")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
    def who_am_i(self):
        print("I am a dog")

mydog = Dog()
mydog.eat()  
```

### Polymorphism 

```
class Dog():
    def __init__(self,name):
        self.name=name
    def speak(self):
         return self.name + " woofs"
      
class Cat():
    def __init__(self,name):
        self.name=name
    def speak(self):
         return self.name + " meows"
              
```

### Abstract Class 

```
class Animal():
    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement")

class Dog(Animal):
    def speak(self):
        return self,name + " says woof"

mydog = Dog()
mydog.speak()
   
```

### Special / dunder methods

```
class Book():
    def __init__(self,title,author,pages):
  
```

1. TO String   
  ```
  def __str__(self):
  ```

2. Length :
  ```
   def __len__(self):
  ```

3. 