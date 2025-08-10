def simple_generators():
    print("Start")
    yield 1
    yield 2
    yield 3
    print("End")
gen = simple_generators()
print(next(gen))
print(next(gen))
print(next(gen))
'''Start
1
2
3'''


