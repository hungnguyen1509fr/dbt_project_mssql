{{ config(
    materialized='table'
) }}

WITH source AS (
    SELECT *
    FROM {{ source('YOUTUBE', 'YOUTUBE_VIDEO_METRICS') }}
),

transformed AS (
    SELECT
        brand AS Team,
        video_id AS Vid_ID,
        title AS Title,
        views AS Count_Views,
        likes AS Count_Likes,
        comments AS Count_Comments,
        published_at AS published_at_ts,
        CAST(published_at AS DATE) AS published_date,
        TO_CHAR(published_at, 'HH24:MI:SS') AS published_time,
        duration,

        -- Extract minutes using basic pattern 'PTxxM'
        COALESCE(
            TRY_TO_NUMBER(
                REGEXP_SUBSTR(duration, 'PT([0-9]+)M', 1, 1, 'e', 1)
            ), 0
        ) AS duration_minutes,

        -- Extract seconds using basic pattern 'xxS'
        COALESCE(
            TRY_TO_NUMBER(
                REGEXP_SUBSTR(duration, '([0-9]+)S', 1, 1, 'e', 1)
            ), 0
        ) AS duration_seconds,

        -- Combine mm:ss
        LPAD(
            COALESCE(
                TRY_TO_NUMBER(REGEXP_SUBSTR(duration, 'PT([0-9]+)M', 1, 1, 'e', 1)), 0
            ), 2, '0'
        ) || ':' || LPAD(
            COALESCE(
                TRY_TO_NUMBER(REGEXP_SUBSTR(duration, '([0-9]+)S', 1, 1, 'e', 1)), 0
            ), 2, '0'
        ) AS duration_mmss

    FROM source
)

SELECT * FROM transformed
