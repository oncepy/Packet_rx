import rx
from rx import operators as ops
from rx.subject import Subject

subject = Subject()

subject_with_filter = subject.pipe(
    ops.filter(lambda i: i < 100),
    ops.map(lambda i: i*1000)
)

subject_with_filter.subscribe(
    lambda i: print("Subscriber 1: {0}".format(i))
)
subject_with_filter.subscribe(
    lambda i: print("Subscriber 2: {0}".format(i))
)

subject.on_next(10)
subject.on_next(50)
subject.on_next(105)
subject.on_next(87)
