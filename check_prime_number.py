def is_prime(number):
    if number <= 1:
        print("Your number is not a prime number!")
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            print("Your number is not a prime number!")
            return False
    print("Your number is a prime number!")
    return True

is_running = True
def main():
    while is_running:
        numberSelected = float(input("Enter your number: "))
        is_prime(numberSelected)
        
main()
