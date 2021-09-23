def main():
    #write your code below this line
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    answer = average(num1, num2, num3, num4)
    print("Average: " + str(answer))

def average(num1, num2, num3, num4):
    total = sum(num1, num2, num3, num4)
    return total / 4

def sum(num1, num2, num3, num4):
    return num1 + num2 + num3 + num4

if __name__ == '__main__':
    main()
