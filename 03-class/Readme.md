### Class and Object Orientation Aspects

 - Class defn / Initializr defn / Instance Attributes
 - Class Attributes
 - Static Methods
 - Class Methods
 - Interactions with inheritance
 - Encapsulation of data within classes - Properties
 - Specializing Properties
 - Designiing for extensibility ( properties )


## Instance vs Class Attributes.
  Class Attributes - shared with all instances of the class.
  ShippingContainer.class_attr_counter


## Static Method Decorator
  - Note no self
  - When just a pure implementation with params no need to access class attributes.  
 ```
 @staticmethod
 def _generate_serial():
     result = ShippingContainer.next_serial
     ShippingContainer.next_serial += 1
     return result
     
 ```
 ## Class Method Decorator
 - Note - cls instead of self
 - When need to access class level attribute
 ```
 @classmethod
 def _generate_serial(cls):
     result = cls.next_serial
     cls.next_serial += 1
     return result    
 ```

### Factory method / varying params to initialize the class
 - Factory method returns an instance of the class. Method name allows callers to express intent and allows construction to be performed with diff combinations of args.
 - cls() is the named contructor that internally calles th init.  


```
@classmethod
def create_empty(cls,ownercode)
    return cls(owner_code,contents=[])
@classmethod
def create_with_items(cls,ownercode,items)
    return cls(ownercode,contents=items)


>> myEmptyContainer = ShippingContainer.create_empty("satbasu")
```

## Behaviour of Class and Static methods in INHERITANCE

#### For Static Method to have polymorphic implementation take over:
 > self._make_bic_code  in the __init__  

Note the _make_bic_code static functions in the child class too has the _make_bic_code
```
from shipping import *
r2 = RefrigeratedShippingContainer("YML",["fish"])
c1 = ShippingContainer("YML",["box"])
c1.bic
'YMLU0013380'
r2.bic
'YMLR0013372'
```

#### Class Method interact with Inheritance ( behave polymorphically )
  note the factorymethods are using the 'cls' 
    

```
from shipping import *
r2 = RefrigeratedShippingContainer.create_empty("YML")
```

1. Now Child Class has overriden Constructor with new param
2. In Python is Child Class is overriding the constructor , the call to super class constructor must be coded explicitly.
3. Have Base class constructors have other args as needed by child class ( Celcsius in this case )


### Properties in python ( Encapsulate Getter and Setter )
 - GETTER = @property
 - SETTER = @propName.setter
 - The prop itself is kept private by self._propname
 - The syntax to set or get values now dont need to call functions but be used
   > GET : print(myObj.celsius)
   > SET : myObj.celsius = 10
 - the getter and setter can have its custom logic

```
class Example
    @property
    def p(self):
        return self._p
    @p.setter
    def p(self,value):
        self._p = value 
```

### Review Concepts

 1. Single Inheritance.
    class SubClass(BaseClass):
     - subClass Init must call base class init ( super() )

2. Type Check Inspection ( ISINSTANCE and ISSUBCLASS )
  >  isinstance()
  >  isinstance(3,int)
  >  isinstance(obj,(float,int))  # if object is one of float or int
  
  > issubclass(IntList,SimpleList)    
  
3. Multiple Inheritance support in python
   - class Subclass (Base1,Base2,Base3)    
   - inherit all methods
   - BaseClass Init: If subclass defines no init , the init of the first base class is called  

4.  Method Resolution Order  [ MRO ]
   - SubClass.__mro__
      

#### Class Decorator
  - How to create your own class decorator


#### Hash and equality
  For object equality comparision so that they can be used rightfully into sets and dict.
  - Immutability is diff to express in python
  - Hashbased collections still require immutable elements
  - Equality and hashing must be consistent.
  
#### Dataclass ( how it can help to acheive immutablity at dataclass object level.)