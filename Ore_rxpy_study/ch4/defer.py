import rx

x = 1
y = 5

integers = rx.range(x, y)
integers.subscribe(lambda i: print(i))

print("\nSetting y = 10\n")
y = 10

integers.subscribe(lambda i: print(i))




