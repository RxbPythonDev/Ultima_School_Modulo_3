iterable = 'UltimaSchool'
iter_obj = iter(iterable)
# try:
#     print(next(iter_obj))
#     print(next(iter_obj))
#     print(next(iter_obj))
#     print(next(iter_obj))
#     print(next(iter_obj))
#     print(next(iter_obj))
#     print(next(iter_obj))
#     print(next(iter_obj))
#     print(next(iter_obj))
#     print(next(iter_obj))
#     print(next(iter_obj))
#     print(next(iter_obj)) # l
#     print(next(iter_obj))
# except StopIteration:
#     print('Deu exception')

for i in iter_obj: # i = next(iter_obj)
    print(i)

print('Fora do for')
