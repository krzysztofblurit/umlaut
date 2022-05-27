class Sets:
    def __init__(self):
        self.exercise_1()
        self.exercise_2()
        self.exercise_3()
        self.exercise_4()
        self.exercise_5()

    @staticmethod
    def exercise_1():
        print("Exercise 1")
        l = list(range(1, 10))
        list_multiple = []
        for n in range(len(l)+1):
            for x in range(n):
                list_multiple.append(n)
        setOfList = set(list_multiple)
        print(list_multiple)

    @staticmethod
    def exercise_2():
        print("Exercise 2")
        set1 = {1,2,3,4,5}
        set2 = {3,4,5,6,7}
        print(set1 & set2)

    @staticmethod
    def exercise_3():
        print("Exercise 3")
        set1 = {1,2,3,4,5}
        set2 = {3,4,5,6,7}
        diff_set = set1.difference(set2)
        print(diff_set)

    @staticmethod
    def exercise_4():
        print("Exercise 4")
        set1 = {1,2,3,4,5}
        set2 = {3,4,5,6,7}
        lackInTwo = set(set1).difference(set2)
        print(lackInTwo)

    @staticmethod
    def exercise_5():
        print("Exercise 5")
        set1 = {1,2,3,4,5}
        set2 = {3,4,5,6,7}
        combineSet = set1.union(set2)
        print(combineSet)

if __name__ == "__main__":
    zadanie = Sets()