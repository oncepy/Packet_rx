import rx
from rx import operators as ops


rx.from_(
    ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]
).pipe(
    ops.map(lambda s: len(s)),
    ops.distinct()
).subscribe(
    lambda i: print(i)
)
