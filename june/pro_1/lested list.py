Result =[]
scorelist = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Result+=[[name,score]]
        scorelist+=[score]
    b=sorted(list(set(scorelist)))[1]

    for a,c in sorted(Result):
        if c==b:
            print(a)


# list program

if __name__ == '__main__':
    N = int(input())
    l = []

    while N > 0:
        command = input()
        currCommand = command.split(" ")

        for i in range(len(currCommand)):
            if i == 0:
                continue
            currCommand[i] = int(currCommand[i])

        if currCommand[0] == "insert":
            l.insert(currCommand[1], currCommand[2])
        elif currCommand[0] == "print":
            print(l)
        elif currCommand[0] == "remove":
            l.remove(currCommand[1])
        elif currCommand[0] == "append":
            l.append(currCommand[1])
        elif currCommand[0] == "sort":
            l.sort()
        elif currCommand[0] == "pop":
            l.pop()
        elif currCommand[0] == "reverse":
            l.reverse()
        N -= 1
