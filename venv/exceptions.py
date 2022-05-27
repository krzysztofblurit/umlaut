import string
class ExceptionsTask:
    def __init__(self):
        self.exercise_1()

    @staticmethod
    def exercise_1():
        range_value = 10
        d = dict({})

        list_values = list(string.ascii_lowercase[0:range_value])
        for n in range(len(list_values)):
            d[n] = list_values[n]

        print(d)
        x=0
        for n in range(20):
            try:
                print(d[x])
                x = x + 1
            except Exception:
                print("No more elements")
                break

if __name__ == "__main__":
    zadanie = ExceptionsTask()