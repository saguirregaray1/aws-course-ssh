CREATE SCHEMA apps_schema;

CREATE TABLE IF NOT EXISTS apps_schema.playstore
(
    app_name character varying COLLATE pg_catalog."default",
    app_id character varying COLLATE pg_catalog."default" NOT NULL,
    category character varying COLLATE pg_catalog."default",
    rating double precision,
    rating_count bigint,
    maximum_installs bigint,
    last_updated character varying COLLATE pg_catalog."default",
    content_rating character varying COLLATE pg_catalog."default",
    ad_supported boolean,
    market_segment character varying COLLATE pg_catalog."default"
)
