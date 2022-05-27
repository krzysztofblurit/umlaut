import string
class Dictionaries:
    def __init__(self):
        self.exercise_1()
        self.exercise_2()
        self.exercise_3()
        self.exercise_4()
        self.exercise_5()

    @staticmethod
    def exercise_1():
        print("Exercise 1")
        list = ["a", "b", "c", "d", "e"]
        dictionary = {key: value for value, key in enumerate(list)}
        print(dictionary)

    @staticmethod
    def exercise_2():
        print("Exercise 2")
        list = ["a", "b", "c", "d", "e"]
        dictionary = {k: v for v, k in enumerate(list)}
        for key in dictionary.keys():
            print(key, '->', dictionary[key])

    @staticmethod
    def exercise_3():
        print("Exercise 3")
        list = ["a", "b", "c", "d", "e"]
        dictionary = {k: v for v, k in enumerate(list)}
        for k, v in dictionary.items():
            print(k, v)

    @staticmethod
    def exercise_4():
        print("Exercise 4")
        n = 50
        def listDiv(n):
            l = []
            for i in range(1, n + 1):
                if n % i == 0:
                    l.append(i)
            return l

        d = dict({})
        for n in range(n):
            d[n] = listDiv(n)

        print(d)

    @staticmethod
    def exercise_5():
        print("Exercise 5")

        range_value = 10
        d = dict({})

        list_values = list(string.ascii_lowercase[0:range_value])
        # print(listv_alues)

        for n in range(len(list_values)):
            if (n % 2) == 0:
                d[n+1] = list_values[n]
        print(d)


if __name__ == "__main__":
    zadanie = Dictionaries()