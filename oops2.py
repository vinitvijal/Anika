class anika:
    def __init__(self) -> None:
        pass

    def sqrt(num):
        return num**0.5
    
while True:
    try:
        n = int(input('Enter a Number : '))
        print(anika.sqrt(n))
        break
    except ValueError:
        print('Wrong Input Try Again...\n\n')

    except:
        print('Another Error')

