import rx
import rx.operators as ops


def add_and_multiply(nums, add_value, multiply_value):
    return nums.pipe(
        ops.map(lambda i: i + add_value),
        ops.map(lambda i: i * multiply_value)
    )


numbers = rx.from_([1, 2, 3]).pipe(
    ops.map(lambda i: i + 1),
    ops.map(lambda i: i * 2)
)


numbers.subscribe(
    on_next=lambda i: print("on_next {}".format(i)),
    on_error=lambda e: print("on_error: {}".format(e)),
    on_completed=lambda: print("on_completed")
)
