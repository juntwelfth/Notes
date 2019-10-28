
# Class

## Pass

- 클래스나 함수, 메소드 내부를 `pass`로 해놓으면 파이썬 컴파일러가 읽지않고 넘어간다.

```py
class CoolClass:
    pass
```

## Instance

- 클래스 인스턴스 생성

```py
class CoolClass:
    pass

instance_cool = CoolClass()
```

## Self

- 파이썬 내 모든 클래스의 메소드는 self라는 argument를 가지고 있어야 한다.

```py
class Dog():
    dog_age = 7

    def my_dog(self):
        print("My Dog is {} yo.".format(self.dog_age))


pitbull = Dog()
pitbull.my_dog()

# prints "My Dog is 7 yo."
```

>Java, Javascript의 this와 같은 역할을 한다.

## Constructors

- `__init__(self)`는 생성자 함수이다.

```py
class Shouter:
    def __init__(self, phrase):
        # phrase가 string이면 대문자로 출력
        if type(phrase) == str:
            print(phrase.upper())

shout1 = Shouter("shout")
# prints "SHOUT"

shout2 = Shouter("let it all out")
# prints "LET IT ALL OUT"
```

## Instance Variables

- 인스턴스 변수

# Empty Class

```py
class FakeDict:
    pass

ins1 = FakeDict()
ins2 = FakeDict()

ins1.fake_var = "Hi Hi"
ins2.fake_var = "12345"

print("{} {}".format(ins1.fake_var, ins2.fake_var)
# prints "Hi Hi 12345"
```

>클래스 변수와 인스턴스 변수는 다르다.

## Attribute Functions

- `hasattr()`, `getattr()` 키워드는 두개의 인자를 받는다.

```py
hasattr(ins1, "fake_attribute")
# returns False

getattr(ins2, "other_fake_attribue", 800)
# returns 800
```

>default return값을 정해줄 수 있다.
>존재하지 않는 변수를 불러오려고 하면 AttributeError가 발생한다.

## Everything is an Object

- `dir()` 키워드를 통해 인자로 전달받은 객체가 특정 변수와 메소드를 가지고 있는지 알 수 있다.

```py
class FakeDict:
    pass

fake_dict = FakeDict()
fake_dict.attribute = "Cool"

dir(fake_dict)
# Prints ['__class__', '__delattr__', '__dict__',
#  '__dir__', '__doc__', '__eq__', '__format__',
#  '__ge__', '__getattribute__', '__gt__',
#  '__hash__', '__init__', '__init_subclass__',
#  '__le__', '__lt__', '__module__', '__ne__',
#  '__new__', '__reduce__', '__reduce_ex__',
#  '__repr__', '__setattr__', '__sizeof__',
#  '__str__', '__subclasshook__', '__weakref__',
#  'attribute']

fun_list = [10, "string", {'abc': True}]

type(fun_list)
# Prints <class 'list'>

dir(fun_list)
# Prints ['__add__', '__class__', [...], 'append',
#  'clear', 'copy', 'count', 'extend', 'index',
#  'insert', 'pop', 'remove', 'reverse', 'sort']
```

>`int`, `float`, `str`, `list`, `dict`는 전부 객체다.

## String Representation

- `__repr__`을 이용해 객체의 대표 스트링을 반환할 수 있다.

```py
class Employee():
    def __init__(self, name):
        self.name = name

argus = Employee("Argus Filch")
print(argus)

# prints "<__main__.Employee object at 0x104e88390>"
```

argus의 주소값을 반환한 것을 볼 수 있다.

```py
class Employee():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

argus = Employee("Argus Filch")
print(argus)
# prints "Argus Filch"
```

>java의 `toString()`과 같은 역할을 한다.

# Inheritance and polymorphism

## Inheritance

- 상속

```py
class User:
    is_admin = False

def __init__(self, username)
    self.username = username

class Admin(User):
    is_admin = True
```

## Exceptions

- `issubclass()` 키워드를 통해 자손인지 확인하고 맞으면 True, 아니면 False를 리턴한다.

```py
issubclass(ZeroDivisionError, Exception)
# Returns True

class KitchenException(Exception):
"""
Exception that gets thrown when a kitchen appliance
isn't working
"""

class MicrowaveException(KitchenException):
"""
Exception for when the microwave stops working
"""

class RefrigeratorException(KitchenException):
"""
Exception for when the refrigerator stops working
"""
```

>KitchenException 예외를 정의하고, 자손 클래스들을 생성했다.

```py
def get_food_from_fridge():
if refrigerator.cooling == False:
    raise RefrigeratorException
else:
    return food

def heat_food(food):
    if microwave.working == False:
        raise MicrowaveException
    else:
        microwave.cook(food)
        return food

try:
    food = get_food_from_fridge()
    food = heat_food(food)
except KitchenException:
    food = order_takeout()
```

>각 함수에 예외를 raise(던지는) 조건문을 넣어줬다.
>냉장고에서 음식을 꺼낼 때 KitchenException 예외가 발생하면 음식을 주문한다.

## Overriding Methods

- 오버라이딩

```py
class User:
    def __init__(self, username, permissions):
        self.username = username
        self.permissions = permissions

    def has_permission_for(self, key):
        if self.permissions.get(key):
            return True
        else:
            return False
```

- `User` 클래스를 정의하고 `__init__` (생성자)에 `permissions` 매개변수를 넣어줬다.
- `permissions`가 `dict`라고 가정하자.
- `User`에는 메소드 `has_permissions_for()`가 있는데, 인자로 주어진 `key`가 `permissions` 에 포함되어 있는지를 확인한다.

```py
class Admin(User):
    def has_permission_for(self, key):
        return True
```

- `User` 클래스의 자손 클래스인 `Admin` 클래스를 선언했다.
- `User`의 메소드와 속성들을 동일하게 가지는데 `has_permissions_for()`를 호출하면 `permissions` dictionary를 체크하지 않는다.

## Super()

- 조상 클래스의 메소드를 호출할 수 있게 해주는 키워드

```py
class Sink:
    def __init__(self, basin, nozzle):
        self.basin = basin
        self.nozzle = nozzle

class KitchenSink(Sink):
    def __init__(self, basin, nozzle, trash_compactor=None):
        super().__init__(basin, nozzle)

    if trash_compactor:
        self.trash_compactor = trash_compactor
```

조상 클래스의 생성자를 호출했다.

## Polymorphism

- 연산자는 상황에 따라 다른 일을 하기도 한다.

```py
# For an int and an int, + returns an int

2 + 4 == 6

# For a float and a float, + returns a float

3.1 + 2.1 == 5.2

# For a string and a string, + returns a string

"Is this " + "addition?" == "Is this addition?"

# For a list and a list, + returns a list

[1, 2] + [3, 4] == [1, 2, 3, 4]
```

## Dunder Methods

- Double Underscore (D-under)
- `__init__`, `__repr__` 외에 더 많은 Dunder Methods가 있다.

```py
class Color:
    def __init__(self, red, blue, green):
        self.red = red
        self.blue = blue
        self.green = green

    def __repr__(self):
        return "Color with RGB = ({red}, {blue},
            {green})".format(red=self.red,
            blue=self.blue, green=self.green)

    def add(self, other):
    # min()으로 self.red + other.red 와 255 중
    # 더 작은 수를 반환
    new_red = min(self.red + other.red, 255)
    new_blue = min(self.blue + other.blue, 255)
    new_green = min(self.green + other.green, 255)

    return Color(new_red, new_blue, new_green)


red = Color(255, 0, 0)
blue = Color(0, 255, 0)

magenta = red.add(blue)
print(magenta)
# Prints "Color with RGB = (255, 255, 0)"
```

- 파이썬에서는 기본적으로 직접 정의한 클래스에 의해 생성된 객체는 연산이 불가능하다.
- 따라서 위와 같이 따로 함수를 정의해주고 `red.add(blue)`처럼 연산을 해줘야한다.

```py
class Color:
    def __add__(self, other):
        """
        Adds two RGB colors together
        Maximum value is 255
        """
        new_red = min(self.red + other.red, 255)
        new_blue = min(self.blue + other.blue, 255)
        new_green = min(self.green + other.green, 255)

        return Color(new_red, new_blue, new_green)

red = Color(255, 0, 0)
blue = Color(0, 255, 0)
green = Color(0, 0, 255)
```

>dunder method `__add__`를 사용하면 객체끼리의 연산이 가능하다.

```py
# Color with RGB: (255, 255, 0)

magenta = red + blue

# Color with RGB: (0, 255, 255)

cyan = blue + green

# Color with RGB: (255, 0, 255)

yellow = red + green

# Color with RGB: (255, 255, 255)

white = red + blue + green
```

## Dunder Methods II

- 파이썬의 내장 data type과 동일한 기능을 제공하는 마법같은 메소드가 있다.

```py
class UserGroup:
    def __init__(self, users, permissions):
        self.user_list = users
        self.permissions = permissions

    def __iter__(self):
        return iter(self.user_list)

    def __len__(self):
        return len(self.user_list)

    def __contains__(self, user):
        return user in self.user_list
```

- `__iter__` : 함수 내부에 `iter()`를 정의해줌으로 user_list를 iterator로 변환시켰다.
그로인해 `for user in user_group` 기능을 사용할 수 있게되었다.

- `__len__` : 함수 내부에 `len()`을 정의해줌으로 `self.user_list` 리스트의 길이를 반환한다.

- `__contains__` : `user in user_group` 키워드를 사용할 수 있게 해준다.

```py
class User:
    def __init__(self, username):
        self.username = username

diana = User('diana')
frank = User('frank')
jenn = User('jenn')

can_edit = UserGroup([diana, frank],
    {'can_edit_page': True})
can_delete = UserGroup([diana, jenn],
    {'can_delete_posts': True})

print(len(can_edit))
# Prints 2

for user in can_edit:
    print(user.username)
    # Prints "diana" and "frank"

if frank in can_delete:
    print("Since when do we allow Frank to delete \
        things? Does no one remember when \
        he accidentally deleted the site?")
```

>파이썬 내장기능처럼 사용할 수 있다.
