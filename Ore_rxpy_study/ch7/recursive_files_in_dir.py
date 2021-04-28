import rx
from rx import operators as ops
import os


def recursive_files_in_directory(folder):

    def emit_files_recursively(observer, scheduler):
        for root, directories, filenames in os.walk(folder):
            for directory in directories:
                observer.on_next(os.path.join(root, directory))
            for filename in filenames:
                observer.on_next(os.path.join(root, filename))

        observer.on_completed()

    return rx.create(emit_files_recursively)


recursive_files_in_directory('../').pipe(
    ops.filter(lambda f: f.endswith('.txt')),
    ops.flat_map(lambda f: rx.from_(open(f, encoding="ISO-8859-1"))),
    ops.map(lambda l: l.strip()),
    ops.filter(lambda l: l != "")
).subscribe(
    on_next=lambda l: print(l),
    on_error=lambda e: print(e)
)
