
a = "abcdefghijqlmnopqrstuvwxyz"
lst = [1,2,3,4,5]

lst[0] = 5
lst[:3] = [9,9,0]


def a_func(b_func): 
    print(b_func(4))

def square(num): 
    return num*num

def custom_filter(lst,filter_func):
    ret_lst = []
    for ele in lst: 
        if filter_func(ele): 
            ret_lst.append(ele)


lst2 = [1,2,3,4,5,6]

if __name__ == "__main__":
    print(a)
    print(lst)
    print(a[::2])

    a_func(square)

    
    print(custom_filter(lst2,lambda x : x%2==0))
    print(custom_filter(lst2,lambda x : x>3))

    f = open("README.md")
    print(f.read())

    f.seek(0)
    print(f.read())

    f.close()

    with open("README.md","r") as fp: 
        fp.read()

    # will throw an error
    # print(fp.seek(0))





