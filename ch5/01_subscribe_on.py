import rx
import rx.operators as ops

scheduler = SomeScheduler()  # 이런 스케줄러는 없다. 어떤 스케줄러 이다라는 예시일 뿐임 다양한 스케줄러가 될수 있다.
numbers = rx.from_([1, 2, 3, 4])

subscription = numbers.pipe(
    ops.map(lambda i: i*2),
    ops.map(lambda i: "number is: {}".format(i)),
    ops.subscribe_on(scheduler)
).subscribe(
    on_next=lambda i: print("on_next {}".format(i)),
    on_error=lambda e: print("on_error: {}".format(e)),
    on_completed=lambda: print("on_completed")
)

