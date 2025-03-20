from db import db

def migrate_up():
  db.execute_sql("""
    DROP TABLE IF EXISTS task_detail;
    CREATE TABLE task_detail (
      id SERIAL NOT NULL,
      task_id INTEGER NOT NULL,
      title TEXT NOT NULL,
      priority_id INTEGER NOT NULL,
      status_id INTEGER NOT NULL,
      staff_id INTEGER NOT NULL,
      created_at TIMESTAMP,
      created_by INTEGER,
      modified_at TIMESTAMP,
      modified_by INTEGER,
      start_date DATE NOT NULL,
      end_date DATE NOT NULL,
      active BOOLEAN DEFAULT TRUE NOT NULL,
      PRIMARY KEY (id),
      UNIQUE (title)
    );
    CREATE INDEX IF NOT EXISTS main_search_key ON task_detail (priority_id,status_id, staff_id);
  """)