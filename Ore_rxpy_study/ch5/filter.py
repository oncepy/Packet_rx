import rx
from rx import operators as ops


rx.from_(
    ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]
).pipe(
    ops.filter(lambda s: len(s) >= 5)
).subscribe(lambda s: print(s))

