import rx
from rx import operators as ops


rx.from_(
    ["Alpha", "Theta", "Kappa", "Beta", "Gamma", "Delta", "Epsilon"]
).pipe(
    ops.map(lambda s: len(s)),
    ops.distinct_until_changed()
).subscribe(
    lambda i: print(i)
)

print()
print('-' * 20)

rx.from_(
    ["Alpha", "Theta", "Kappa", "Beta", "Gamma", "Delta", "Epsilon"]
).pipe(
    ops.distinct_until_changed(lambda s: len(s))
).subscribe(
    lambda i: print(i)
)
