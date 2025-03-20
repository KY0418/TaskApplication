from db import db

def migrate_up():
  db.execute_sql("""
    DROP TABLE IF EXISTS status;
    CREATE TABLE status (
      id SERIAL NOT NULL,
      name TEXT NOT NULL,
      active BOOLEAN DEFAULT TRUE NOT NULL,
      PRIMARY KEY (id),
      CONSTRAINT unique_status_name UNIQUE (name)
    );
    INSERT INTO status (name, active) values 
     ('完了',true),
     ('未完了',true),
     ('着手',true),
     ('待機',true);
  """)