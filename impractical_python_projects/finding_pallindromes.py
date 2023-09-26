def find_palindromes():
    list_10 = []
    with open('utils/dictionary.txt', 'r') as file:
        # while True:
        #     content = file.readline()
        #     if len(list_10) > 10:
        #         break
        #     list_10.append(content.strip())
        for _ in range(10):
            content = file.readline()
            if not content:
                break
            list_10.append(content.strip())
    print(list_10)


if __name__ == '__main__':
    find_palindromes()
