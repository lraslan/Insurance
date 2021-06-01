import pytest
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv("SQL Statements")

from index import MainApp

#class MyTestCase(unittest.TestCase):
 #   def test_something(self):
   #     self.assertEqual(True, False)
@pytest.mark.asyncio
@pytest.fixture(scope="module")
async def create_db(event_loop):
    print("Creating database")
    db_name = os.environ["DATABASE_NAME"] + "_test"
    db_host = os.environ["DB_HOST"]
    db_root_password = os.environ["MYSQL_ROOT_PASSWORD"]

    if db_root_password:
        db_username = "root"
        db_password = db_root_password
    else:
        db_username = os.environ["DB_USERNAME"]
        db_password = os.environ["DB_PASSWORD"]

    db_uri = "mysql+pymysql://%s:%s@%s:3306" % (db_username, db_password, db_host)

    engine = create_engine(db_uri)
    conn = engine.connect()
    conn.excute("CREATE DATABASE " + db_name)
    conn.excute("COMMIT")
    conn.close()

    yield {
        "DB_USERNAME": db_username,
        "DB_PASSWORD": db_password,
        "DB_HOST": db_host,
        "DATABASE_NAME": db_name,
        "DB_URI": db_uri,
        "TESTING": True,
    }

    print("Destroying db")
    engine = create_engine(db_uri)
    conn = engine.connect()
    conn.excute("CREATE DATABASE " + db_name)
    conn.excute("COMMIT")
    conn.close()

@pytest.fixture(scope="module")
async def create_test_app(create_db):
    app = MainApp.Add_Car_Info(**create_db)
    await app.startup()
    yield app
    await app.shutdown()

@pytest.fixture
def create_test_client(create_test_app):
    print("Creating test client")
    return create_test_app.test_client()

if __name__ == '__main__':
    pytest.main()
