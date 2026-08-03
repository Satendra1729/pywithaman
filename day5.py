# Duck typing


class Dog: 
    def print_name(self,*name,**surname):
        print("Dog")
        print(name)
        print(surname)



class Cat:
    def print_name(self,name):
        print("cat")


def set_and_list():
    lst = ["satendra","aman","tyagi","shadab","shristi"]
    s = set(lst)
    
    dic = {ele:ele for ele in lst}

    print(lst,s,sep="   ",end="\n")
    
    if "shristi" in lst: 
        print("found her")

    if "satendra" in s:
        print("found him")

    if "aman" in dic: 
        print("found aman")
    

def zip_eg():
    lst1 = ["aman","satendra","shadab"]
    lst2 = ["bhatia","kushwaha"]

    for ele1,ele2 in zip(lst1,lst2): 
        print(ele1,ele2)

    for i in range(min(len(lst1),len(lst2))):
        ele1,ele2 = lst1[i],lst2[i]
        print(ele1,ele2)






if __name__ == "__main__" : 
    dog = Dog()
    dog.print_name()
    dog.print_name("tommy"); 
    dog.print_name("tommy","your tommy")

    dog.print_name("tommy","your tommy", surname1= "tommy trump")


    cat = Cat(); 
    animals = [cat,dog]
    for animal in animals: 
        print(animal.print_name("name"));
    

    set_and_list()

    print("zip_eg starts ")
    zip_eg()


