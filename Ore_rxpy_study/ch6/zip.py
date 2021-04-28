import rx
from rx import operators as ops


letters = rx.from_(["A", "B", "C", "D", "E", "F"])
numbers = rx.range(1, 5)

letters.pipe(
    ops.zip(numbers),
    ops.map(lambda z: "{0}-{1}".format(z[0], z[1]))
).subscribe(
    lambda i: print(i)
)
