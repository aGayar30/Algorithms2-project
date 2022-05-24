switches = []

def Off(start, end):
    n = end - start + 1
    if n == 1:
        toggle(end)
    elif n == 2:
        toggle(start)
        toggle(end)
    else:
        Off(start + 2, end)
        toggle(start)
        On(start + 2, end)
        Off(start + 1 , end)

def On(start, end):
    n = end - start + 1
    if n == 1:
        toggle(end)
    elif n == 2:
        toggle(end)
        toggle(start)
    else:
        On(start + 1, end)
        Off(start + 2, end)
        toggle(start)
        On(start +2, end)

def toggle(i):
    if switches[i] == 1:
        switches[i] = 0
    else:
        switches[i] = 1
    print(switches)

def main():
    global switches
    n = int(input("Enter number of switches: "))
    switches = [1] * n
    print(switches)
    Off(0, n - 1)

if __name__ == "__main__":
    main()
