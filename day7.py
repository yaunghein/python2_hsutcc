def custom_generator(data):
    index = 0
    for el in data:
        yield index, el
        index += 1


yan = custom_generator({'as': 'b'})
print(next(yan))
