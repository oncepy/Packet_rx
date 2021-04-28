import rx
from rx import operators as ops


rx.from_(
    ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]
).pipe(
    ops.to_list()
).subscribe(
    lambda s: print(s)
)

