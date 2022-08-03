CREATE TABLE IF NOT EXISTS templates (
       id               INTEGER NOT NULL,
       tag              TEXT NOT NULL,
       version          TEXT NOT NULL,
       content          TEXT NOT NULL,
       is_active        INTEGER NOT NULL DEFAULT 1,
       PRIMARY KEY      (id)
);
