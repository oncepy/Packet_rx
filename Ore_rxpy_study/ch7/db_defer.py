from sqlalchemy import create_engine, text
import rx
from rx import operators as ops

engine = create_engine('sqlite:///rexon_metals.db')
conn = engine.connect()

def get_all_customers():
    stmt = text("SELECT * FROM CUSTOMER")
    return rx.defer(lambda x: rx.from_(conn.execute(stmt)))


my_source = get_all_customers()

my_source.subscribe(lambda r: print(r))
my_source.subscribe(lambda r: print(r))
