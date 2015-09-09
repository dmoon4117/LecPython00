#a={1:'a'}
#a[2]='b'
#a['name']='pey'
#a[3]=[1,2,3]
#del a['name']

#print(a['1'])
#a={'name':'pey','phone':'0119993323','birth':'1118'}
#b=a.keys()
#b=list(a.keys())
#print(b)

#a={'name':'pey','phone':'0119993323','birth':'1118'}
#b=a.values()
#b=list(a.values())
#print(b)

#a={'name':'pey','phone':'0119993323','birth':'1118'}
#b=a.items()
#print(b)


#get.get 해보기
#movie1={'홍길동':{'베테랑':'5.0', '암살':'4.5'}}
#movie2={'고길동':{'베테랑':'4.0', '암살':'4.2'}}

#movie1.get("홍길동").get("베테랑")

#print(movie1.get.get) 
#point1=list(movie1.values())
#print(point1)
#point2=list(movie2.values())
#print(point2)

#answer=input("would you like express shipping?")
#lower사용해서 대소문자 상관없이 출력되게 해보기
#if answer == "yes" :
#    print("That will be an extra $10")

#a=[(1,2),(3,4),(5,6)]
#for(first,last) in a:
#    print(first+last)


##한번더해보기
#for i in range(2,10):
#    print('%d단'%i)
#    for j in range(1,10):
#        print('%d * %d = %d'% (i,j,i*j),end=' ')
#        print('')

#a=[1,2,3,4]
#resuit=[]
#resuit=[num*3 for num in a]
#print(resuit)

#import turtle
#for steps in range(4):
#    turtle.forward(100)
#    turtle.right(90)
# 사각형을 그린다


#import turtle
#for steps in range(4):
#    turtle.forward(100)
#    turtle.right(90)
#    for moresteps in range(4):
#        turtle.forward(50)
#        turtle.right(90)
# 사각형안에 4개의 사각형을 그린다

#import turtle
#nSides = 5
#for steps in range(nSides):
#    turtle.forward(100)
#    turtle.right(360/nSides)
#    for moresteps in range(nSides):
#        turtle.forward(50)
#        turtle.right(360/nSides)
# 오각형안에 5개의 오각형을 그린다 중앙에 별이 생김

#import turtle 
#for steps in ['red','blue','green','black']:
#    turtle.colormode(steps)
#    turtle.forward(100)
#    turtle.right(90)

prompt="""
1. Add
2. Del
3. List
4. Quit

Enter number: """

number=0
while number !=4:
    print(prompt, end="")
    number=int(input())