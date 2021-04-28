import rx
from rx import operators as ops


rx.from_(
    ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]
).pipe(
    ops.filter(lambda s: len(s) >= 5),
    ops.take(2)
).subscribe(
    on_next=lambda s: print('R: ' + s),
    on_error=lambda e: print('on_error' + e),
    on_completed=lambda: print('Done!!'),
)
