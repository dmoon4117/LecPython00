#fileName = "greenjoa.txt."
#WRITE = "w"
#myFile = open(fileName, "w")
#myFile.write("hi")

#myFile.close() #파일을 열었으면 꼭 닫아줘야한다.

#fileName = "text.txt"
#READ = "r"
#myFile = open(fileName, mode = READ)
#cotent = myFile.readlines()
#for line in content:
#    print(line)
#myFile.close()

 
#fileName = "donghyun.txt"
#with open(fileName, "w+") as myFile :
#    myFile.write("201111262 김동현")
#    myFile.write("201111261 곽민기")



#fileName = "donghyun.txt"

#with open(fileName, "r") as myFile :
#    content = myFile.read() 
#    print(content)  

#fileName = "파일입출력예제1.txt"

#with open(fileName, "r") as myFile :
#    content = myFile.read() 
#    print(content)  
  

#fileName = "파일입출력예제1.txt"

#with open(fileName, "r") as myFile :
#    for content in myFile : #줄단위로
#      print(content)  

#fileName = "파일입출력예제1.txt"
#fileName2 = "Monica.txt"

#with open(fileName, "r") as myFile, open(fileName2, "w") as monica :
#    for content in myFile : #줄단위로
#        (role, etc) = content.strip().split(":") # :를 기준으로 자른다 
#        if ( role == "Monica") :                 #strip함수
#            monica.write(etc)
#            monica.write("\n") #줄바꿈

#fileName = "파일입출력예제2.txt"
#fileName2 = "Monica.txt"


#with open(fileName, "r") as myFile, open(fileName2, "w") as monica :
#    for content in myFile :  
#        (role, etc) = content.strip().split(":",1)  
#        if ( role == "Monica") :                  
#            monica.write(etc)
#            monica.write("\n")  


#fileName = "파일입출력예제2.txt"
#fileName2 = "Monica.txt"
#roles = [] #빈리스트

#with open(fileName, "r") as myFile, open(fileName2, "w") as monica :
#    for content in myFile :  
#        (role, etc) = content.strip().split(":",1)  
#        roles.append(role) #리스트에 role를 추가
#print(roles)
 
#import pickle #두가지함수를 통해 파일을 저장하고 다시 불러올수 있다.
#fileName = "파일입출력예제2.txt"
#fileName2 = "Monica.txt"
#roles = []  

#with open(fileName, "r") as myFile, open(fileName2, "wb") as monica : #pickle 바이너리형태
#    for content in myFile :  
#        (role, etc) = content.strip().split(":",1)  
#        roles.append(role)
#    pickle.dump(roles, monica)
  
#with open(fileName2, "rb") as monica :
#    result = pickle.load(monica)
#    print(result)
