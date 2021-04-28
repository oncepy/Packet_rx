import rx
from rx import operators as ops

letters = rx.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"])
intervals = rx.interval(1.0)

letters.pipe(
    ops.zip(intervals),
    ops.map(lambda z: z[0])
).subscribe(
    lambda s: print(s)
)

input("Press any key to quit\n")


