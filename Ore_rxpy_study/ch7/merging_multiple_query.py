from sqlalchemy import create_engine, text
import rx
from rx import operators as ops

engine = create_engine('sqlite:///rexon_metals.db')
conn = engine.connect()


def get_all_customers():
    stmt = text("SELECT * FROM CUSTOMER")
    return rx.from_(conn.execute(stmt))


def customer_for_id(customer_id):
    stmt = text("SELECT * FROM CUSTOMER WHERE CUSTOMER_ID = :id")
    return rx.from_(conn.execute(stmt, id=customer_id))


# Query customers with IDs 1, 3, and 5
rx.from_(
    [1, 3, 5]
).pipe(
    ops.flat_map(lambda id: customer_for_id(id))
).subscribe(
    lambda r: print(r)
)
