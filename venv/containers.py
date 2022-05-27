class ListExercise:
    def __init__(self):
        self.exercise_1()
        self.exercise_2()
        self.exercise_3()
        self.exercise_4()
        self.exercise_5()
        self.exercise_6()

    @staticmethod
    def exercise_1():
        print("Exercise 1")
        list = []
        n = 0
        for x in range(10):
            list.append(n)
            n=n+1
        print(list)


    @staticmethod
    def exercise_2():
        print("Exercise 2")
        list = ["a", "b", "c", "d", "e"]
        for count, letter in enumerate(list):
            print(count, letter)

    @staticmethod
    def exercise_3():
        print("Exercise 3")
        list_alphabet = ["a", "b", "c", "d", "e"]
        list_numbers = [1,2,3,4,5]
        list_alphabet.extend(list_numbers)
        print(list_alphabet)

    @staticmethod
    def exercise_4():
        print("Exercise 4")
        list_alphabet = ["a", "b", "c", "d", "e"]
        list_numbers = [1, 2, 3, 4, 5]
        list_index = []
        for x in range(len(list_alphabet)):
            list_index.append(list_alphabet[x])
            list_index.append(list_numbers[x])
        print(list_index)

    @staticmethod
    def exercise_5():
        print("Exercise 5")
        list = []
        n = 0
        for x in range(10):
            list.append(n)
            n = n + 1
        list.reverse()
        print(list)

    @staticmethod
    def exercise_6():
        print("Exercise 6")
        l = []
        n = 0
        for x in range(10):
            l.append(n)
            n=n+1
        for i in l[:]:
            if i % 2 != 0:
                l.remove(i)
        print(l)

if __name__ == "__main__":
    zadanie = ListExercise()

