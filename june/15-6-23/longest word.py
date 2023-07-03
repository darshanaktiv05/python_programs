# fourth program
def get_words():
    N = int(input("How many words you want to enter: "))
    li = []

    for i in range(N):
        word = input("enter words: ")
        li.append(word)

    print("the list you have entered is: ", li)
    print("the longest word of list is: ", min(li))
    print("the longest word's length os: ", len(min(li)))


get_words()
