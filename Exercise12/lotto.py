import random

def generate():
    numbers = set()
    while len(numbers) < 6:
        numbers.add(random.randint(1, 50))
    return numbers

def main():
    lottery_numbers = generate()
    print("Lottery numbers:")
    for number in lottery_numbers:
        print(number)

if __name__ == "__main__":
    main()

# Simplified to;

lottery_numbers = random.sample(range(1, 51), 6)

print("Lottery numbers:")
for number in lottery_numbers:
    print(number)