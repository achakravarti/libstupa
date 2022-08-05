-- update template
-- archive template
-- restore template
-- delete template
--
-- list templates
-- list templates csv
-- load template


-- create new template
INSERT INTO templates (tag, version, content, assets_path, is_archived)
VALUES (?, ?, ?, ?, FALSE);
