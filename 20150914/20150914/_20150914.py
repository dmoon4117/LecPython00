#def main():
#    printMessage()
#    return
##main() = printMessage()
#def printMessage():
#    print("Hello World!")
#    return
##printMessage() = print("Hello Wolrd!")

#main()
#def main():
#    names = ["greenjoa1","greemjoa2","greenjoa3"]
#    newName = input("Enter last guest: ")
#    names.append(newName)
#    #append 리스트의 마지막에 삽입
#    printNames(names)
#    return

#def printNames(names):
#    for name in names:
#        print(name)
#    return

#main()

def sum_mul(chioce, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result = result + i
        elif chioce == "mul":
            result = 1
            for i in args: