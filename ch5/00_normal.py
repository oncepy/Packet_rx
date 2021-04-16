import rx
import rx.operators as ops

numbers = rx.from_([1, 2, 3, 4])

subscription = numbers.pipe(
    ops.map(lambda i: i*2),
    ops.map(lambda i: "number is: {}".format(i))
).subscribe(
    on_next=lambda i: print("on_next {}".format(i)),
    on_error=lambda e: print("on_error: {}".format(e)),
    on_completed=lambda: print("on_completed")
)
