from sqlalchemy import create_engine, text
import rx
from rx import operators as ops

engine = create_engine('sqlite:///rexon_metals.db')
conn = engine.connect()


def get_all_customers():
    stmt = text("SELECT * FROM CUSTOMER")
    return rx.from_(conn.execute(stmt))


get_all_customers().subscribe(lambda r: print(r))

