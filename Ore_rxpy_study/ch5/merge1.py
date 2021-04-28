import rx
from rx import operators as ops

source1 = rx.interval(1.0).pipe(
    ops.map(lambda i: "Source 1: {0}".format(i))
)
source2 = rx.interval(0.5).pipe(
    ops.map(lambda i: "Source 2: {0}".format(i))
)
source3 = rx.interval(0.3).pipe(
    ops.map(lambda i: "Source 3: {0}".format(i))
)

rx.merge(source1, source2, source3).subscribe(lambda s: print(s))

# keep application alive until user presses a key
input("Press any key to quit\n")

