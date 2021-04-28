import rx
import rx.operators as ops

numbers = rx.from_([1, 2, 3, 4]).pipe(
    # ops.flat_map(lambda i: rx.from_(range(i, i+2)))
    ops.flat_map(lambda i: range(i, i+2))
    # ops.map(lambda i: list(range(i, i+2)))
)
# 위 두가지 방식의 차이점은??

numbers.subscribe(
    on_next=lambda i: print("on_next {}".format(i)),
    on_error=lambda e: print("on_error: {}".format(e)),
    on_completed=lambda: print("on_completed")
)
