def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child

first=parent(1)
print(first)
print(first())
second=parent(2)
print(second)
print(second())