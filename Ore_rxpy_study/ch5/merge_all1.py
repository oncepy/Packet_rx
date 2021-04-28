import rx
from rx import operators as ops

items = ["134/34/235/132/77", "64/22/98/112/86/11", "66/08/34/778/22/12"]

rx.from_(items).pipe(
    ops.map(lambda s: rx.from_(s.split("/"))),
    ops.merge_all(),
    ops.map(lambda s: int(s))
).subscribe(
    lambda i: print(i)
)
