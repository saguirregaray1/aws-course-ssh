CREATE SCHEMA apps_schema;

CREATE TABLE apps_schema.apps (
  app_name VARCHAR,
  app_id VARCHAR,
  category VARCHAR,
  rating NUMERIC,
  rating_count INTEGER,
  maximum_installs INTEGER,
  is_free BOOLEAN,
  last_updated VARCHAR,
  content_rating VARCHAR,
  ad_supported BOOLEAN,
  CONSTRAINT pk_apps PRIMARY KEY (app_id)
);