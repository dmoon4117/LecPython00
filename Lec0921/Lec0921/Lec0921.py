#class Service:
#    secret = '영구는 배꼽이 두 개다'
#    def sum(self, a, b):
#        result = a + b
#        print('%s + %s = %s 입니다.' % (a, b, result))

#pey = Service()
#print(pey.secret)

#pey.sum(1,1) 
#Service.sum(pey,1,1)

#class movie:
#    title = "베테랑"
#    director = "류승완"
#    def __inif__(self, title, director):
#        self.title = title
#        self.director = director

#    def showinfo(self):
#        print(self.title + " " + self.director)
#show = movie("베테랑","류승완")
#show2 = movie()

#Movie.personal #perosnal 이란 속성이 없으므로 오류 

#class movie: 
#    '''영화 클래스입니다.'''
#    title = "스타워즈"
#    director = "조지 루카스"
#    def __init__(self, title, director):
#        self.title = title
#        self.director = director
#        print(self.title + " 생성자 호출 ")
    
#    def __del__(self):
#        print(self.title + " 소멸자 호출 ")

#    def showinfo(self):
#        print(self.title + " " + self.director)
#m1 = movie("베테랑1","류승완1");
#m2 = movie("베테랑2","류승완2");
#m3 = movie("베테랑3","류승완3");



#class movie: 
#    '''영화 클래스입니다.'''
#    title = "스타워즈"
#    director = "조지 루카스"
#    def __init__(self, title, director):
#        self.title = title
#        self.director = director
#        print(self.title + " 생성자 호출 ")
    
#    def __del__(self):
#        print(self.title + " 소멸자 호출 ")

#    def showinfo(self):
#        print(self.title + " " + self.director)
#m1 = movie("베테랑1","류승완1");
#m2 = movie("베테랑2","류승완2");
#m3 = movie("베테랑3","류승완3");
#m4 = movie("베테랑4","류승완4");
#print(type(m4))
#m4 = m3
#m4.showinfo()
#파이썬도 참조형 대입연산을 하면 똑같은 주소를 가리키게 된다

#class movie: 
#    '''영화 클래스입니다.'''
#    title = "스타워즈"
#    director = "조지 루카스"
#    def __init__(self, title, director):
#        self.title = title
#        self.director = director
#        print(self.title + " 생성자 호출 ")
    
#    def __del__(self):
#        print(self.title + " 소멸자 호출 ")

#    def showinfo(self):
#        print(self.title + " " + self.director)
#m1 = movie("베테랑1","류승완1");
#m2 = movie("베테랑2","류승완2");
#m3 = movie("베테랑3","류승완3");
#m4 = movie("베테랑4","류승완4");
#print(type(m4))
#m4 = m3
#print(id(m4))
#print(id(m3))
#m4.showinfo()

#class movie: 
#    '''영화 클래스입니다.'''
#    title = "스타워즈"
#    director = "조지 루카스"
#    def __init__(self, title, director):
#        self.title = title
#        self.director = director
#        print(self.title + " 생성자 호출 ")
    
#    def __del__(self):
#        print(self.title + " 소멸자 호출 ")

#    def showinfo(self):
#        print(self.title + " " + self.director)
    
         
#m1 = movie("베테랑1","류승완1");
#m2 = movie("베테랑2","류승완2");
#m3 = movie("베테랑3","류승완3");
#m4 = movie("베테랑4","류승완4");
#print(type(m4))
#m4 = m3
#print(id(m4))
#print(id(m3))
#m4.showinfo()

class movie: 
    '''영화 클래스입니다.'''
    count = 0  
    title = "스타워즈"
    director = "조지 루카스"
    def __init__(self, title, director):
        self.title = title
        self.director = director
        movie.count+=1 
        print(self.title + " 생성자 호출 ")
    
    def __del__(self):
        print(self.title + " 소멸자 호출 ")

    def showinfo(self):
        print(self.title + " " + self.director)

    @staticmethod 
    def showcount():
        print(movie.count)

    @classmethod 
    def showcount2(cls):
        print(cls.count)
 
m1 = movie("a","b")
m2 = movie("c","d")
m3 = movie("c","d")
m3 = movie("c","d")
m4 = movie("c","d")
m5 = movie("c","d")

movie.showcount()
movie.showcount2()