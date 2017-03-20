# BEST PRACTICE - BEFORE
def average(numbers):
    total = 0
    for num in numbers:
        total = total + num
    avg = total / len(numbers)
    return avg

prices = [29, 21, 55, 10]
result = average(prices)
print(result)

# BEST PRACTICE - AFTER
def average(numbers):
    total = 0
    for num in numbers:
        total = total + num
    avg = total / len(numbers)
    return avg

def main():
    prices = [29, 21, 55, 10]
    result = average(prices)
    print(result)

main()
