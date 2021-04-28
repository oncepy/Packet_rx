import rx
from rx import operators as ops

items = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]

rx.from_(items).pipe(
    ops.group_by(lambda s: len(s)),
    ops.flat_map(lambda grp: grp.pipe(ops.to_list()))
).subscribe(
    lambda i: print(i)
)

