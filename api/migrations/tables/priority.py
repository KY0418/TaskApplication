from db import db

def migrate_up():
  db.execute_sql("""
    DROP TABLE IF EXISTS priority;
    CREATE TABLE priority (
      id SERIAL NOT NULL,
      name TEXT NOT NULL,
      active BOOLEAN DEFAULT TRUE NOT NULL,
      PRIMARY KEY (id),
      CONSTRAINT unique_priority_name UNIQUE (name)
    );
    INSERT INTO priority (name, active) values 
      ('高', true),
      ('中', true),
      ('低', true),
      ('無', true);
  """)