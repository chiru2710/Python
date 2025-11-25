'''a funtion is self contained block of code .
function are mainly used for code resuability,modularity'''
def ipl():
    print("ipl is is an indian T20 cricket leaguge")
ipl()
#function with aruguments
def add(x,y):
    return (x+y)
result= add(2,5)
print(result)
'''we have four types of arguments they are 
1.positional arguments
2.default arguments
3.keyword argument
4.arbitary argument
a.multi positional argument
b.multiple key word arguments'''
print("\npositional arguments")
def name(name,age):
    print(f"my name is {name} my age is {age}")
name("chiru",20)
#default arugments
def favourite_ipl_teams(team="SRH", captain="Unknown"):
    print(f"My favourite IPL team is {team} & the team captain is {captain}")
favourite_ipl_teams()
favourite_ipl_teams("RCB", "Cummains")
#keyword argument
def full_name(firstname, lastname):
    print(f"{firstname} = 'chiranjeevi', {lastname} = 'jangili'")
full_name("firstname", "lastname")
#aribtary arguments
#multi positional arguments
def calculate_sum(*numbers):
    return sum(numbers)
result = calculate_sum(10, 20, 30, 40)
print(f"Total Sum: {result}")
#multiple key word arguments
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
display_info(name="Chiranjeevi", age=21, city="Hyderabad", profession="Developer")
#scopes
#acessing global scoped varaibles in local scope
name="chiru"
age=20
role="junior full stack developer"
def hello():
    print(name)
    print(role)
    print(age)
hello()