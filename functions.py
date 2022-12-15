def main():
    print("running")
    print(f'1 plus 2 is {addTwoNumers(1,2)}')
    print(f'2 minus 1 is {subtractTwoNumbers(1,2)}')
    
    
def addTwoNumers(num1, num2):
    return num1+num2

def subtractTwoNumbers(num1, num2):
    return num2 - num1

if __name__ == '__main__':
    main()

