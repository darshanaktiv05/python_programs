# ninth program
def get_words():
    N = int(input("How many words you want to enter: "))
    li = []

    for i in range(N):
        word = input("enter words: ")
        li.append(word)

    print("the list you have entered is: ", li)
    print(sorted(li))


get_words()
