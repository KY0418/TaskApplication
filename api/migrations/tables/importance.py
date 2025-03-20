from db import db

def migrate_up():
  db.execute_sql("""
    DROP TABLE IF EXISTS importance;
    CREATE TABLE importance (
      id SERIAL NOT NULL,
      name TEXT NOT NULL,
      priority_id INTEGER NOT NULL,
      real_priority_num INTEGER,
      active BOOLEAN DEFAULT TRUE NOT NULL,
      PRIMARY KEY (id),
      CONSTRAINT unique_importance_name UNIQUE (name)
    ); 
    INSERT INTO importance (name, priority_id, active) values 
     ('highest', 1, true),
     ('high', 2, true),
     ('medium', 3, true),
     ('low', 4, true);
  """)