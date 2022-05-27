class Lambda:
    def __init__(self):
        self.exercise_1()
        self.exercise_2()

    @staticmethod
    def exercise_1():
        print("Exercise 1")

        x = range(0,20)
        f = list(filter(lambda n: n % 2 == 0, x))
        print(f)
        y = list(filter(lambda n: n % 2 == 1, x))
        print(y)



    @staticmethod
    def exercise_2():
        print("Exercise 2")
        x = range(0,10)



        sequences = [10, 2, 8, 7, 5, 4, 3, 11, 0, 1]
        filtered_result = map(lambda x: x * x, range(0,10))
        print(list(filtered_result))

if __name__ == "__main__":
    zadanie = Lambda()