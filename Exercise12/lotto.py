import random

def generate_lottery_numbers():
    numbers = set()
    while len(numbers) < 6:
        numbers.add(random.randint(1, 50))
    return numbers

def main():
    lottery_numbers = generate_lottery_numbers()
    print("Lottery numbers:")
    for number in lottery_numbers:
        print(number)

if __name__ == "__main__":
    main()
