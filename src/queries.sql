

-- create new template
INSERT INTO templates (tag, version, content, assets_path, is_archived)
VALUES (?, ?, ?, ?, 0);


-- update template
UPDATE templates
SET tag = ?, version = ?, content = ?, assets_path =?
WHERE id = ?;


-- archive template
UPDATE templates
SET is_archived = 1
WHERE id = ?;


-- restore template
UPDATE templates
SET is_archived = 0
WHERE id = ?;


-- delete template
DELETE FROM templates
WHERE id = ?;


-- list active templates
SELECT id, tag, version
FROM templates
WHERE is_archived = 0;


-- list archived templates
SELECT id, tag, version
FROM templates
WHERE is_archived = 1;


-- load template
SELECT id, tag, version, content, assets_path, is_archived
FROM templates
where id = ?;
