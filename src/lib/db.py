import sqlite3
from typing import List, Optional, Tuple
from .error import DatabaseError


class Db:
    SQL_INIT = '''
    CREATE TABLE IF NOT EXISTS templates (
       id               INTEGER PRIMARY KEY,
       name             TEXT NOT NULL,
       version          TEXT NOT NULL,
       content          TEXT NOT NULL,
       is_archived      BOOLEAN NOT NULL DEFAULT 0,
       UNIQUE           (id, tag) ON CONFLICT ABORT
    );
    CREATE INDEX IF NOT EXISTS idx_templates__tag ON templates (tag);
    CREATE INDEX IF NOT EXISTS idx_templates__version ON templates (version);
    '''
    SQL_LIST_ACTIVE = '''
    SELECT id, name, version, content
    FROM templates
    WHERE is_archived = FALSE;
    '''
    SQL_LIST_ARCHIVED = '''
    SELECT id, name, version, content
    FROM templates
    WHERE is_archived = TRUE;
    '''
    SQL_LOAD = '''
    SELECT id, name, version, content, is_archived
    FROM templates
    WHERE id = ?;
    '''
    SQL_ID_EXISTS = '''
    SELECT exists(
        SELECT 1
        FROM templates
        WHERE id = ?
    );
    '''
    SQL_ID_ACTIVE = '''
    SELECT exists(
        SELECT 1
        FROM templates
        WHERE id = ? AND is_active = TRUE
    );
    '''
    SQL_ID_ARCHIVED = '''
    SELECT exists(
        SELECT 1
        FROM templates
        WHERE id = ? AND is_active = FALSE
    );
    '''
    SQL_ID_FIND = '''
    SELECT id
    FROM templates
    WHERE name = ? AND version = ?
    );
    '''
    SQL_CREATE = '''
    INSERT INTO templates (id, name, version, content)
    VALUES (?, ?, ?, ?);
    '''
    SQL_UPDATE = '''
    UPDATE templates
    SET name = ?, version = ?, content = ?
    WHERE id = ?;
    '''
    SQL_ARCHIVE = '''
    UPDATE templates
    set is_archived = TRUE
    WHERE id = ?;
    '''
    SQL_RESTORE = '''
    UPDATE templates
    set is_archived = FALSE
    WHERE id = ?;
    '''
    SQL_DELETE = '''
    DELETE
    FROM templates
    WHERE id = ?;
    '''

    @staticmethod
    def init():
        """Initialises the database."""
        Db.exec(Db.SQL_INIT, None)

    @staticmethod
    def exec(sql: str, params: Optional[Tuple]) -> List:
        """Executes a query with optional parameters."""
        try:
            conn = sqlite3.connect('libstupa.db')
            cur = conn.cursor()
            if params is not None:
                res = cur.execute(sql, params).fetchall()
            else:
                res = cur.execute(sql).fetchall()
            cur.close()
            conn.close()
            return res
        except sqlite3.Error as e:
            raise DatabaseError(e.args[0])
