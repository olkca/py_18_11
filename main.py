from random import randint

test_list1 = []
test_list2 = []
i = 0
while i in range(10):
    test_list1.append(randint(0, 10))
    test_list2.append(randint(0, 10))
    i += 1
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

max_all = max(test_list1 + test_list2)
min_all = min(test_list1 + test_list2)
print("The maximum of both lists is : " + str(max_all))
print("The minimum of both lists is : " + str(min_all))
