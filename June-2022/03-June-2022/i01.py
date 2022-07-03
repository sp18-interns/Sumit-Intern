# data = [1, 2, 9, 8, 3, 4, 7, 6, 5]


def get_first(data):
    for index in range(0, len(data), 3):
        return (data[index])
        #return (get_first(data))
        #return (data[0])


a = get_first([1, 3, 5, 7, 9, 2, 4, 6, 8])
print(a)
