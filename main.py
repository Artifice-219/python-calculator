def main_func(x, y, op):
    if op == '+' :
      return add(first_num, second_num)
    elif op == '-' :
      return sub(first_num, second_num)
    elif op == '*' :
      return mult(first_num, second_num)
    elif op == '/' :
      return div(first_num, second_num)
    
def add(x,y) :
    return x + y

def sub(x,y) :
    return x - y

def mult(x,y) :
    return x * y

def div(x,y):

    if divisor_check(y) :
      return x / y
    else :
       return print('Cannot divide by zero')

def driver():
   choice = str(input("Would you like to contiue ? : [ Y/N ]"))

   if choice == 'y' or 'Y' :
      return True
   elif choice == 'n' or 'N' :
      return False
   else :
    #   defaulting to false
      return False

def divisor_check(num) :
   if num <= 0 :
      return False
   else :
      return True    
      
while True :
   
   print('Simple calculator')
   first_num = float(input('Enter first number: '))
   second_num = float(input('Enter second number: '))
   operator = input('Choose between [ + - * / ] : ')
    
   result = main_func(first_num, second_num, operator)

   print(f'Result : {result}')

   next = str(input('Would you like to continue ? [y/n]'))
   
   if next == 'n' :
      break




