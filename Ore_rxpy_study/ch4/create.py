import rx


def push_numbers(observer, scheduler):
    observer.on_next(100)
    observer.on_next(300)
    observer.on_next(500)
    observer.on_completed()


rx.create(
    push_numbers
).subscribe(
    on_next=lambda i: print("on_next: ", i),
    on_error=lambda e: print("on_error: ", e),
    on_completed=lambda: print("on_completed ")
)

