
-- The templates table holds the actual templates. Each template is uniquely
-- identified by a combination of its tag and version. However, we use a
-- separate integer primary for performance reasons. Templates may be archived,
-- i.e. they are soft-deleted, and the is_archived flag tracks this. The actual
-- template content is stored in the content field. We choose to abort in case
-- there is a unique constraint violation; this is the default behaviour but we
-- are making it explicit.

CREATE TABLE IF NOT EXISTS templates (
       id               INTEGER PRIMARY KEY,
       tag              TEXT NOT NULL,
       version          TEXT NOT NULL,
       content          TEXT NOT NULL,
       is_archived      INTEGER NOT NULL DEFAULT 0,
       UNIQUE           (id, tag) ON CONFLICT ABORT
);


-- Create indices on the tag and version columns. We normally search by tag and
-- sort by both tag and version.

CREATE INDEX idx_templates__tag ON templates (tag);

CREATE INDEX idx_templates__version ON templates (version);
