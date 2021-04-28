import rx

letters = rx.from_(['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon'])


letters.subscribe(
    on_next=lambda value: print(value),
    on_error=lambda error: print(f'Error occurred {error}'),
    on_completed=lambda: print('completed..')
)





