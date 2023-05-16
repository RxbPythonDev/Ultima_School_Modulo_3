valor_string = 'UltimaSchool'
objeto_iter = iter(valor_string)

# for item in objeto_iter:
#     print(item)

while True:
    try:
        # Iterate by calling next
        item = next(objeto_iter)
        print(item)
    except StopIteration:
        # exception will happen when iteration will over
        break