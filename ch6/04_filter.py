import rx
import rx.operators as ops

numbers = rx.from_([1, 2, 3, 4, 5]).pipe(
    ops.filter(lambda i: 1 < i < 4)
)

numbers.subscribe(
    on_next=lambda i: print("on_next {}".format(i)),
    on_error=lambda e: print("on_error: {}".format(e)),
    on_completed=lambda: print("on_completed")
)
