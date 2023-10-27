from collections import defaultdict


def find_palindromes():
    count = defaultdict(int)
    for k, v in count.items():
        print(k, v)


def teach_something():
    print("I am th best!!")


if __name__ == '__main__':
    # teach_something()
    # teach_something()
    # find_palindromes()
    nums = [1, 1, 3, 4]
    l = sorted(nums)
    index_dic = defaultdict(list)
    for i in range(0, len(nums)):
        index_dic[nums[i]].append(i)
    print(index_dic)
