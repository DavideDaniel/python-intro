some_list = [1, 3, 4, 5, 6, 2, 1, 5]

set()
# set()

asdf = set()

set(some_list)
# {1, 2, 3, 4, 5, 6}

another_list = list(set(some_list))

another_list
# [1, 2, 3, 4, 5, 6]

numbers = {1,3,5,7}

numbers2 = {1,3}

numbers2.issubset(numbers)
# True

numbers2.issuperset(numbers)
# False

numbers.issuperset(numbers2)
# True

