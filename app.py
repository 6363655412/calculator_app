from cal_func import do_addition,do_div
from cal_func import do_sub
from multiple import do_mul
from area import do_area
def main():
    print('''Welcome calculator app..
          1.add
          2.sub
          3.mul
          4.Div''')

    user_input = input("select the function")
    a = int(input("value of A"))
    b = int(input("value of B"))

    result = 0
    if user_input == "1":
        result =  do_addition(a,b)
    elif user_input == "2":
        result = do_sub(a,b)
    elif user_input == "4":
        result = do_div(a,b)

if __name__ == "__main__":
    main()



