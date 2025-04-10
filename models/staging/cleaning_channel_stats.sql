{{ config(
    materialized='table',
    schema='staging'
) }}

WITH source AS (
    SELECT *
    FROM {{ source('YOUTUBE', 'YOUTUBE_CHANNEL_METRICS') }}
),

transformed AS (
    SELECT
        channel_id AS id,
        channel_title AS team,
        subscribers AS subscribers,
        total_views AS no_views,
        total_videos AS no_videos,
        country,
        published_at AS published_at_ts
    FROM source
)
SELECT * FROM transformed;