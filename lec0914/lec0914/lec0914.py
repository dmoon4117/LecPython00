#def main():
#    names = getNames()
#    printNames(names)
#    return

#def getNames():
#    names = ["greenjoa1","greenjoa2","greenjoa3"]
#    newName = input("Enter last guest: ") 

#def sum_and_mul(a,b):
#    return a+b, a*b

#sum, mul = sum_and_mul(10,30)
#print(sum, mul)

#(coding:cp949)
#유니코드 인코딩

#def printData(data):
#    for item in data:
#        print(item)
        

#data = ["홍길동",["베테랑", "암살"],"고길동",["암살"]]
#printData(data) 


#def printData(data):
#    for item in data:
#        if isinstance(item, list):
#            for items in item:
#                print(items)
#        else:
#            print(item)
        

#data = ["홍길동",["베테랑", "암살"],"고길동",["암살"]]
#printData(data) 

#재귀함수

   
#data = ["홍길동",["베테랑",["류승완",["황정민",["류아인"]]]]]

#import printData

#data = ["홍길동",["베테랑", "암살"],"고길동",["암살"]]
#printData.printData(data)

import os

print(os.getcwd())
#os.mkdir("sample")
os.chdir(".//sample")
#os.system("python setup.py sdist")
os.system("python setup.py install")