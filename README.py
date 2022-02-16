#Simple Calculater

def add(x, y):
    return x+y
    
def sub(x, y):
    return x-y
    
def mul(x, y):
    return x*y
    
def div(x, y):
    return x/y
    
    
print("Select Operation")    
print("1.Add")
print("2.Subtract")
print("3.Multiple")
print("4.Divide")
  
    
while True:

    choise=input("Enter (1/2/3/4):")
    
    if choise in ('1', '2','3', '4'):
        num1=float(input("Enter First Number:"))
        num2=float(input("Enter Second Number:"))
        
        if choise=='1':
            print(num1, '+',num2,'=',add(num1,num2))
            
        elif choise=='2':
            print(num1, '-',num2,'=',sub(num1, num2))
            
        elif choise=='3':
            print(num1, '*',num2,'=',mul(num1, num2))
            
        elif choise=='4':
            print(num1, '/',num2,'=',div(num1, num2))
            
        next_step=input("Lets do next calculation?(yes/no) :")
        
        if next_step=='no':
            break
            
    else:
        print("Invalid Input")
   
