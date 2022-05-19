'''
#Print
print(5)
print(-10)
print(3.14)
print(5+3)
print(2*8)
print((3+3)*3)
print('Balloon')
print('B'*5)
print(5>10)
print(5<10)
print(True)
print(False)
print(not True)
print(not (5<10))
print(not (5>10))
'''

'''
#Variable
#Please introduce your pet~
animal = 'puppy'
name = 'whity'
age = 4
hobby = 'take a walk'
is_adult = age > 3

print('Our '+animal+"'s name is "+name)
print(name+" is "+str(age)+' years old and he loves to '+hobby)
print('Is '+name+' adult? '+str(is_adult))
'''

'''
#연산자
print(1+1)  #2
print(2**3) #8
print(9%6)  #3
print(9//6) #1
print(10>3) #True
print(6 >= 5)   #True
print(6 >= 6)   #True
print(6 >= 7)   #False
print(3==3)     #True
print(6+3 == 9) #True
print(1 != 3)   #True
print(not(1 != 3))   #True
print((3>0) and (5>3))  #True
print((3>0) & (5>3))  #True
print((3>0) or (5<3))  #True

number = 2*3*4
print(number)   #24
number = number+2
print(number)   #26
number *= 2
print(number)   #52
number /= 13
print(number)   #4
number %= 3
print(number)   #1
'''

'''
#숫자처리함수
print(abs(-5))  #5 절댓값
print(pow(4,2)) #16 4**2
print(max(5,12))#12 Max
print(min(5,12))#5  Min
print(round(3.14))  #3  반올림
print(round(3.56))  #4  반올림

from math import *
print(floor(4.99))  #4  내림
print(ceil(4.99))   #5  올림
print(sqrt(16))     #4  제곱근
'''

'''
#Random
from random import *
print(random()) #0.0~1.0 Random Value
print(random()*10)  #0.0~10.0 Random Value
print(int(random()*10)) #0~10 Random Integer Value
print(int(random()*10)+1) #1~10 Random Integer Value

print(int(random()*45)+1)   #Lottery Random Number
print(randrange(1,46))      #Lottery Random Number
print(randint(1,45))        #Lottery Random Number
'''

'''
#Random Quiz
date = randint(4,28)
print('오프라인 스터디 모임 날짜는 매월',str(date)+'일로 선정되었습니다.')
'''

'''
#문자열(4-1, 46:58)
sentence = "I'm a Boy"
print(sentence)
sentence1 = 'Python is Easy'
print(sentence1)
sentence2 = """
I'm a boy
and Python is easy to Learn"""
print(sentence2)
'''

'''
#Slicing
jumin = '990112-1213136'
print("Sex : "+ jumin[7])
print('DOB : '+ jumin[:6])      #처음부터 6직전까지
print('7자리 :', jumin[7:])     #7부터 끝까지
print('7자리 :', jumin[-7:])    #뒤에서 7번째부터 끝까지
'''

'''
#문자열 처리 함수
python = 'Python is Amazing'
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace('Python','java'))

index = python.index('n')
print(index)
index = python.index('n',index+1)
print(index)

print(python.find('n'))
print(python.find('java'))
#print(python.index('java'))

print(python.count('n'))
'''

'''
#문자열 포맷
print('a'+'b')
print('a','b')

#1
print('나는 %d살입니다.' %20)
print('나는 %s을 좋아해요.' %'파이썬')
print('Apple은 %c로 시작해요.' %'A')
print('나는 %s살입니다.' %20)
print('나는 %s색과 %s색을 좋아해요.' %('파란','빨간'))

#2
print('나는 {}살입니다.'.format(20))
print('나는 {}색과 {}색을 좋아해요.'.format('파란','빨간'))
print('나는 {0}색과 {1}색을 좋아해요.'.format('파란','빨간'))
print('나는 {1}색과 {0}색을 좋아해요.'.format('파란','빨간'))

#3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = '빨간'))

#4
age = 20
color = '빨간'
print(f'나는 {age}살이며, {color}색을 좋아해요')
'''

'''
#탈출 문자 \
print("백문이 불여일견 백견이 불여일타")
print("백문이 불여일견\n백견이 불여일타")   #줄바꿈 \n
print("저는 '나도코딩'입니다.")
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.") 

print("Red Apple\rPine")    #\r: 커서를 맨 앞으로 이동
print("Redd\bApple")        #\b: 백스페이스(한글자 삭제)
print("Red\tApple")         #\t: tab
'''

'''
#Quiz) 사이트별로 비밀번호를 만드는 프로그램
#예) http:\\naver.com
#Rule1 : http:\\ 부분은 제외 => naver.com
#Rule2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
#Rule3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내'e'갯수 + "!"로 구성

#My Answer
site = "http://naver.com"
r1 = site[7:-4]
print(r1)
password = r1[0:3]+str(len(r1))+str(r1.count('e'))+"!"
print(password)

#Answer
url = "http://naver.com"
r1 = url.replace("http://",'')
print(r1)
r2 = r1[:r1.index('.')]
print(r2)
password = r2[:3] + str(len(r2)) + str(r2.count('e'))+'!'
print(f"{url}의 비밀번호는 {password}입니다.")
'''

'''
#List
subway1 = 10
subway2 = 20
subway3 = 30
subway = [10,20,30]

subway = ['A','B','C']
print(subway)
print(subway.index('B'))    #index("")
subway.append('D')          #append("")
print(subway)
subway.insert(1, 'E')       #insert(index, "")
print(subway)
# print(subway.pop())         #pop()->맨뒤를 뽑아오기
# print(subway)               #뽑은 객체는 사라짐
# print(subway.pop(1))        #pop(index) -> index제외
# print(subway)
subway.append('A')
print(subway)
print(subway.count('A'))    #count

num_list = [2,6,7,1,3]
num_list.sort()             #sort()                 
print(num_list)
num_list.reverse()          #reverse()
print(num_list)
# num_list.clear()            #clear()
# print(num_list)

mix_list = ['a',20,False]
print(mix_list)
num_list.extend(mix_list)
print(num_list)
'''

'''
#Dictionary
cabinet ={3:'C', 100:'CJ'}
print(cabinet[3])       #dict[key]]
print(cabinet.get(3))   #dict.get(key)
# print(cabinet[5])     
# #dict[key]는 key에 없는 값을 입력하면 오류
print(cabinet.get(5, 'Empty'))  
#dict.ger(key)는 key에 없는 값을 입력하면 Default Value

print(3 in cabinet)     # in cabinet
print(5 in cabinet)

cabinet = {'A3':'C', 'A100':'CJ'}
print(cabinet)
cabinet['A4'] ='D'  #Insert
print(cabinet)
cabinet['A3'] = 'c' #Update
print(cabinet)
del cabinet['A3']   #Delete
print(cabinet)

print(cabinet.keys())   #keys
print(cabinet.values()) #values
print(cabinet.items())  #items
cabinet.clear()         #clear
'''

'''
#Tuple
#Tuple은 Insert, Update, Delete 불가
menu = ("Cutlet","Cheese")
print(menu[0])
print(menu[1])
#menu.add("Fish")
(a,b,c) = (1,2,3)
print(a,b,c)
'''

'''
#Set(집합)
#중복 불가, 순서 없음
my_set = {1,2,3,4,5,5,5,}
print(my_set)
java = {'a','b','c'}
python = set(['a','d']) #set(list) 리스트의 집합화
print(java&python)  #교집합
print(java.intersection(python))    #교집합
print(java|python)    #합집합
print(java.union(python))   #합집합
print(java-python)      #차집합
print(java.difference(python))  #차집합
python.add('e')     #add
print(python)
python.remove('e')  #remove
print(python)
'''

'''
#자료구조의 변경
menu = {"Coffee","Milk","Juice"}
print(menu, type(menu))
menu = list(menu)
print(menu, type(menu))
menu = tuple(menu)
print(menu, type(menu))
menu = set(menu)
print(menu, type(menu))
'''

'''
#Quiz
from random import *
id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
shuffle(id)
print(id)
chicken = id[0]
coffee = sample(id[1:20],3)
print("-- 당첨자 발표 --")
print("치킨 당첨자 :",str(chicken))
print("커피 당첨자: ",coffee)
print("-- 축하합니다 --")

#Answer
from random import *
users = list(range(1,21)) #1~20 생성(type = 'range')
print(users)
shuffle(users)
print(users)

winners = sample(users,4)
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {}".format(winners[0]))
print("커피 당첨자 : {}".format(winners[1:]))
print("-- 축하합니다 --")
'''

'''
#if(6-1, 1:57:30)
weather = "Rain"
weather = "Snow"
weather = input("How's weather today?")
if weather == "Rain":
    print("Unbrella")
elif weather == "MicroDust":
    print("Mask")
else:
    print("Good To Go!")

temp = int(input("How's temperature today?"))
if 30 <= temp:
    print("It's to hot today. Stay in your home.")
elif 10 <= temp and temp < 30:
    print('Nice Weather!')
elif 0 <= temp < 10:
    print("Take your coat. It's quite cold Oustside")
else:
    print("It's really cold outside.")
'''

'''
#for
for waiting_no in [0,1,2,3,4]:
    print("Waiting : {}".format(waiting_no))
for waiting_no in range(5): #0,1,2,3,4
    print("Waiting : {}".format(waiting_no))
for waiting_no in range(1,6): #1,2,3,4,5
    print("Waiting : {}".format(waiting_no))
'''

'''
#while
customer = "Thor"
index = 5
while index >= 1:
    print("{0}, your coffee is ready. {1} left.".format(customer, index))
    index -= 1
    if index == 0:
        print("Your Coffee is disposed.")

# customer = "Iron Man"
# index = 1
# while True:
#     print("{0}, your coffee is ready. Called {1}time.".format(customer, index))
#     index +=1

customer = 'YB'
person = 'Unkown'
while person != customer:
    print("{}, your coffee is ready!".format(customer))
    person = input("What's your name?")

#Continue, Break
absent = [2,5]
nobook = [7]
for student in range(1,11):
    if student in absent:
        continue
    if student in nobook:
        print("Class is over. Come to my office, {}.")
        break
    print("{}, Read page 3".format(student))
'''

'''
#For문 in one line
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

students = ["Ironman","Thor","Groot"]
students = [len(i) for i in students]
print(students)

students = ["Ironman","Thor","Groot"]
students = [i.upper() for i in students]
print(students)

#Quiz 5
import random
passenger = {}
count = 0
for i in range(1,51):
    passenger[i] = random.randint(5,51)
    if 5 < passenger[i] < 15:
        print(f"[O] {i}번째 손님 (소요시간 : {passenger[i]}분)")
        count += 1
    else:
        print(f"[ ] {i}번째 손님 (소요시간 : {passenger[i]}분)")
print("총 탑승 승객: {}분".format(count))
'''

'''
#Function
def open_accuont():
    print("새로운 계좌가 생성되었습니다.")
open_accuont()

def deposit(balance, money):
    print(f"입금이 완료되었습니다. 잔액은 {balance+money} 원입니다.")
    return balance+money

def withdraw(balance, money):
    if balance >= money:
        print(f"출금이 완료되었습니다. 잔액은 {balance-money} 원입니다.")
        return balance - money
    else:
        print(f"잔액이 부족합니다. 잔액은 {balance}원입니다.")

def withdrawatnight(balance, money):
    commision = 100
    return commision, balance - money - commision
balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 200)
commision, balance = withdrawatnight(balance, 500)
print("수수료 {}원이며, 잔액은 {}원입니다.".format(commision, balance))
'''

'''
#Default Value(7-3)
def profile(name, age, main_lang):
    print("이름: {}\n나이 : {}\n주 사용 언어: {}"\
        .format(name, age, main_lang))

profile('a',20,'Python')
profile('b',25,'Java')

def profile(name, age = 17, main_lang='Python'):
    print("이름: {}\n나이 : {}\n주 사용 언어: {}"\
        .format(name, age, main_lang))

profile('a')
profile('b')

#Function using Keyword(7-4)
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = 'a', main_lang='Python', age = '20')

#가변 인자 Function
def profile(name, age, lang1, lang2, lang3, lang4):
    print(f"Name: {name}, Age: {age}", end=" ")
    print(lang1, lang2, lang3, lang4)

profile('YB',20,"Python","Java","C++","R")
profile('AB',25,"Kotlin","Swift",'','')

def profile(name, age, *language):  #*은 가변인자
    print(f"Name: {name}, Age: {age}", end=" ")
    for lang in language:
        print(lang, end = " ")
    print()

profile('YB',20,"Python","Java","C++","R")
profile('AB',25,"Kotlin","Swift")
'''

'''
#Local Variable & Global Variable(7-6)
gun = 10
# def checkpoint(soldiers):
#     global gun
#     gun = gun - soldiers
#     print("[함수 내] 남은 총: {}".format(gun))

# print("전체 총: {}".format(gun))
# checkpoint(2)
# print("남은 총: {}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총: {}".format(gun))
    return gun

print("전체 총: {}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총: {}".format(gun))
'''

'''
#Quiz6
def std_weight(height, gender):
    if gender == 'male':
        std = round((height/100)**2*22,2)
        print("키 {}cm 남자의 표준 체중은 {}kg입니다."\
        .format(height, std))
        return std
    elif gender == 'female':
        std = round((height/100)**2*21,2)
        print("키 {}cm 여자의 표준 체중은 {}kg입니다."\
        .format(height, std))
        return std
std_weight(166,'female')
'''

'''
#표준 출력(8-1)
print('a','b', sep = " vs ")
print('a','b', sep = " vs ", end="?\n")
print('무엇')

import sys
print("a","b",file=sys.stdout)
print("a","b",file=sys.stderr)

scores = {"Math":0, "English":50, "Computer":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4))

for num in range(1,21):
    print("대기번호: "+ str(num).zfill(3))

#표준 입력(8-1)
answer = input("아무 값이나 입력하세요: ")
print("입력하신 값은", answer, "입니다.")
'''

'''
#출력 포맷(8-2)
#빈 자리는 빈공간, 오른쪽 정렬, 10자리 공간 확보
print("{0: >10}".format(500))
#양수일 땐 +, 음수일 땐 - 로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
#왼쪽 정렬, 빈칸 -로 채움
print("{0:-<+10}".format(-500))
#3자리 마다 , 찍기
print("{0:,}".format(10000000000000000))
#3자리 마다 , 찍기/ 부호 붙이기
print("{0:+,}".format(10000000000000000))
print("{0:+,}".format(-10000000000000000))

print("{0:^<+30,}".format(10000000000000))
#소수점 출력
print("{0}".format(5/3))
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3))
'''

'''
#파일 입출력(8-3)
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 0", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding='utf8')
# score_file.write("과학 : 80\n")
# score_file.write("코딩 : 100")
# score_file.close()

score_file = open("score.txt", "r", encoding='utf8')
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding='utf8')
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

score_file = open("score.txt", "r", encoding='utf8')
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

score_file = open("score.txt", "r", encoding='utf8')
lines = score_file.readlines()
for line in lines:
    print(line)
score_file.close()
'''

'''
#Pickle(8-4)
import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름": "박명수", "나이": 30, "취미": ["축구","골프"]}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()
'''
'''
#With(8-5)
import pickle
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬 재미없어ㅓ")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
'''
'''
#Quiz7
for i in range(1,5):
    with open(f"{i}주차.txt","w",encoding="utf8") as report:
        report.write(f"- {i} 주차 주간보고 - \
            \n부서:\n이름:\n업무 요약:\n")
'''
'''
#Class(9-1)
name = "Marine"
hp = 40
damage = 5
print("{} 유닛이 생성되었습니다.".format(name))
print("체력 {},  공격력 {}\n".format(hp, damage))

tank_name = "Tank"
tank_hp = 150
tank_damage = 35
print("{} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {},  공격력 {}\n".format(tank_hp, tank_damage))

def attack(name, location, damage):
    print("{} : {} 방향으로 공격. [공격력 {}]".\
        format(name, location, damage))
attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
'''
'''
#__init__(9-2)
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {},  공격력 {}\n".format(self.hp, self.damage))

marine1 = Unit("Marine", 40, 5)
marine2 = Unit("Marine", 40, 5)
tank = Unit("Tank", 150, 35)
'''
'''
#member variable(9-3)
wraith1 = Unit("Wraith", 80, 5)
print("유닛 이름: {}, 공격력: {}".\
    format(wraith1.name, wraith1.damage))

wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{}은 현재 클로킹 상태입니다.".format(wraith2.name))
'''
'''
#Method(9-4)
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{}: {} 방향으로 적군을 공격합니다. [공격력 {}]".\
            format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{}: {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print(f"{self.name}: 현재 체력은 {self.hp}입니다.")
        if self.hp <= 0:
            print(f"{self.name}: 파괴되었습니다.")

firebat1 = AttackUnit("Firebat", 50, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)
'''
'''
#상속(9-5)
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        print("{} 유닛이 생성되었습니다.".format(self.name))
        print("체력: {}\n".format(self.hp))

class AttackUnit(Unit): #상속
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{}: {} 방향으로 적군을 공격합니다. [공격력 {}]".\
            format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{}: {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print(f"{self.name}: 현재 체력은 {self.hp}입니다.")
        if self.hp <= 0:
            print(f"{self.name}: 파괴되었습니다.")

#다중 상속(9-6)
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print(f"{name}: {location} 방향으로 날아갑니다. [속도: {self.flying_speed}]")

class FlyableAttackUnit(AttackUnit, Flyable):   #다중상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)
valkyire = FlyableAttackUnit("Valkyrie", 200, 6, 5)
valkyire.fly(valkyire.name, "3시")
'''
'''
#Method Overriding(9-7)
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{} 유닛이 생성되었습니다.".format(name))
        print("체력: {}\n".format(self.hp))
    def move(self, location):
        print("[지상 유닛 이동]")
        print(f"{self.name}: {location} 방향으로 이동합니다. [속도: {self.speed}]")
        
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    def attack(self, location):
        print("{}: {} 방향으로 적군을 공격합니다. [공격력 {}]".\
            format(self.name, location, self.damage))
    def damaged(self, damage):
        print("{}: {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print(f"{self.name}: 현재 체력은 {self.hp}입니다.")
        if self.hp <= 0:
            print(f"{self.name}: 파괴되었습니다.")

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print(f"{name}: {location} 방향으로 날아갑니다. [속도: {self.flying_speed}]")

class FlyableAttackUnit(AttackUnit, Flyable):   #다중상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

vulture = AttackUnit("Vulture", 80, 10, 20)
battlecrusier = FlyableAttackUnit("Battlecrusied", 500, 25, 3)
vulture.move("11시")
battlecrusier.move("9시")
'''
'''
#Pass(9-8)
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass

supply_depot = BuildingUnit("Supply Depot", 500, "7시")

def game_start():
    print("게임을 시작합니다.")
def game_over():
    pass
game_start()
game_over()
'''
'''
#Super(9-9)
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        self.location = location
#Super는 다중상속에서 오류 발생
class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()

dropship = FlyableUnit()
#다중 상속은 직접 상속시켜야함
'''
'''
#Quiz8
class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(self.location, self.house_type, self.deal_type,\
            self.price, self.completion_year)

house = []
h1 = House("강남","아파트","매매","10억","2010년")
h2 = House("마포","오피스텔","전세","5억","2007년")
h3 = House("송파","빌라","월세","500/50","2000년")
house.append(h1)
house.append(h2)
house.append(h3)

print(f"총 {len(house)}대의 매물이 있습니다.")
for h in house:
    h.show_detail()
'''
'''
#예외 처리(10-1)
try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요: ")))
    nums.append(int(input("두 번째 숫자를 입력하세요: ")))
    #nums.append(int(nums[0]/nums[1]))
    print(f"{nums[0]}/{nums[1]} = {nums[2]}")
except ValueError:
    print("Error! 잘못된 값을 입력하였습니다!")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print(err)
'''
'''
#에러 발생시키기(10-2)
try:
    print("나누기 전용 계산기입니다.")
    num1 = (int(input("첫 번째 숫자를 입력하세요: ")))
    num2 = (int(input("두 번째 숫자를 입력하세요: ")))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값: {}, {}".format(num1, num2))
    print(f"{num1} / {num2} = {int(num1/num2)}")
except ValueError:
    print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한자리 숫자만 입력하세요.")
    print(err)
'''
'''
#사용자 정의 예외처리(10-3)
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

try:
    print("나누기 전용 계산기입니다.")
    num1 = (int(input("첫 번째 숫자를 입력하세요: ")))
    num2 = (int(input("두 번째 숫자를 입력하세요: ")))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값: {}, {}".format(num1, num2))
    print(f"{num1} / {num2} = {int(num1/num2)}")
except ValueError:
    print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("한자리 숫자만 입력하세요.")
    print(err)
except Exception as err:
    print(err)
#Fianlly(10-4)
finally:
    print('계산기를 이용해 주셔서 감사합니다.')
'''
'''
#Quiz9
class SoldOutError(Exception):
    pass
chicken = 20
waiting = 1
while(True):
    try:
        print(f"[남은 치킨: {chicken}]")
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken:
            print("재고가 부족합니다.")
        elif order <= 0:
            raise ValueError
        else:
            print(f"[대기번호 {waiting}손님] {order}마리 주문이 완료되었습니다.")
            waiting += 1
            chicken -= order
            if chicken == 0:
                raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되었습니다.")
        break
'''
'''
#Module(11-1)
#import theater
#from theater import *
#import theater as the

from theater import *
price(3)
price_morning(4)
price_soldier(5)
'''
'''
#Package(11-2)
from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VitenamPackage()
trip_to.detail()
'''
'''
#__all__(11-3)
from travel import *
trip_to = vietnam.VitenamPackage()
trip_to.detail()
trip_to = thailand.ThailandPackage()    #__all__에 없음
trip_to.detail()
'''
'''
#module직접 실행(11-4)
from travel import thailand
trip_to = thailand.ThailandPackage()
trip_to.detail()
'''
'''
#Packcage, Module Location(11-5)
import inspect
import random
from travel import thailand

print(inspect.getfile(random))
print(inspect.getfile(thailand))
'''
'''
#pip install(11-6)
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
#pip install
#pip install --m upgrade
#pip uninstall
'''
'''
#내장 함수(11-7)
language = input("무슨 언어를 좋아하세요?")
print(f"{language}은 아주 좋은 언어입니다!")

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random
# print(dir())
# import pickle
# print(dir())
print(dir(random))

lst = [1,2,3]
print(dir(lst))

name = 'jin'
print(dir(name))
#google -> list of python builtins
'''
'''
#외장함수(11-8)
#google -> list of python module
# glob: 경로 내의 폴더/ 파일 목록 조회(윈도우 dir)
# import glob
# print(glob.glob("*.py"))

# os: 운영체제에서 제공하는 기본 기능
import os
# print(os.getcwd())  #현재 디렉토리
# folder = "sample_dir"
# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) #폴더생성
#     print(folder, "폴더를 생성하였습니다.")
# print(os.listdir())

# time: 시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S "))
import datetime
print("오늘 날짜는 ",datetime.date.today())
today = datetime.date.today()
td = datetime.timedelta(days=100)
print("100일!", today+td)
'''

#Quiz10
import byme
byme.sign()
