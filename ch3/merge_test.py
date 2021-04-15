import rx
import rx.operators as ops

numbers = rx.from_([1, 2, 3, 4])
strings = rx.from_(["one", "two", "three", "four"])

print("Merge from class static method:")
rx.merge(numbers, strings).subscribe(
    on_next=lambda i: print("item: {}".format(i)),
    on_error=lambda e: print("error: {}".format(e)),
    on_completed=lambda: print("completed")
)
