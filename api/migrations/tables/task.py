from db import db

def migrate_up():
  db.execute_sql("""
                DROP TABLE IF EXISTS task;
                CREATE TABLE task (
                  id SERIAL NOT NULL,
                  category_id INTEGER NOT NULL,
                  active BOOLEAN DEFAULT TRUE NOT NULL,
                  PRIMARY KEY (id)
                 ); 
  """)