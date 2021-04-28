import rx
from rx import operators as ops

# Using Observable.range()
letters = rx.range(1, 10)
letters.subscribe(lambda value: print(value))


# Using Observable.just()
greeting = rx.just("Hello World!")
greeting.subscribe(lambda value: print(value))

rx.empty().subscribe(
    on_next=lambda s: print(s),
    on_completed=lambda: print("Done!")
)
