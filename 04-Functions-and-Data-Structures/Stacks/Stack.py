s = []
length = int(input("Set stack size: "))


def push():
    if len(s) == length:
        print("Stack Overflow")
    else:
        x = int(input("Enter value to insert into stack: "))
        s.append(x)
        print("Value appended :", x)


def pop():
    if len(s) == 0:
        print("Stack Underflow")
    else:
        print("Popped value:", s.pop())


def peak():
    if len(s) == 0:
        print("Stack Underflow")
    else:
        print("Top value:", s[-1])


def display():
    if len(s) == 0:
        print("Stack is empty")
    else:
        for i in range(-1, -len(s) - 1, -1):
            # for i in range(len(s) - 1, -1, -1):
            print(s[i])


if __name__ == "__main__":
    while True:
        print("\n1.PUSH, 2.POP, 3.PEAK, 4.DISPLAY, 5.EXIT\n")
        c = int(input("Enter your response: "))
        if c == 1:
            push()
        elif c == 2:
            pop()
        elif c == 3:
            peak()
        elif c == 4:
            display()
        else:
            break
