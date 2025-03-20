from db import db

def migrate_up():
  db.execute_sql("""
    DROP TABLE IF EXISTS staff;
    CREATE TABLE staff (
      id SERIAL NOT NULL,
      name VARCHAR(20) NOT NULL,
      code TEXT NOT NULL,
      active BOOLEAN DEFAULT TRUE NOT NULL,
      PRIMARY KEY (id),
      CONSTRAINT unique_staff_name UNIQUE (name),
      CONSTRAINT unique_staff_code UNIQUE (code)
      ); 
    INSERT INTO staff (name, code, active) values 
     ('Administerator', '00', true),
     ('あいうえお', '01', true),
     ('かきくけこ', '02', true);
  """)