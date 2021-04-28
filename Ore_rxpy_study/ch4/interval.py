import rx
from rx import operators as ops


rx.interval(1.0).pipe(
    ops.map(lambda i: "{0} Mississippi".format(i))
).subscribe(
    lambda value: print(value)
)

# Keep application alive until user presses a key
input("Press any key to quit")

