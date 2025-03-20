from db import db 

def migrate_up():
  db.execute_sql("""
    CREATE OR REPLACE FUNCTION set_created_at()
      RETURNS TRIGGER AS $$
      BEGIN 
        NEW.created_at := NOW();
      END;
      $$ LANGUAGE plpgsql;

    CREATE OR REPLACE FUNCTION set_updated_at()
      RETURNS TRIGGER AS $$
      BEGIN 
        NEW.modified_at := NOW();
      END;
      $$ LANGUAGE plpgsql;

    CREATE TRIGGER before_insert_set_created_at
      BEFORE INSERT ON task_detail
      FOR EACH ROW
      EXECUTE FUNCTION set_created_at();

    CREATE TRIGGER before_update_set_updated_at
      BEFORE UPDATE ON task_detail
      FOR EACH ROW
      EXECUTE FUNCTION set_updated_at();                
  """)