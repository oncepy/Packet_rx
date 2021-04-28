import rx
from rx import operators as ops

rx.from_(
    ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]
).pipe(
    ops.group_by(lambda s: len(s)),
    ops.flat_map(lambda grp: grp.pipe(
        ops.count(),
        ops.map(lambda ct: (grp.key, ct))
    )),
    ops.to_dict(lambda key_value: key_value[0], lambda key_value: key_value[1])
).subscribe(
    lambda i: print(i)
)

