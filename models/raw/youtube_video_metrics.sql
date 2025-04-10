-- models/raw/youtube_video_metrics.sql

CREATE OR REPLACE TABLE RAW.YOUTUBE_VIDEO_METRICS AS
SELECT 
    $1::TEXT AS brand,
    $2::TEXT AS video_id,
    $3::TEXT AS title,
    $4::TIMESTAMP_NTZ AS published_at,
    $5::NUMBER AS views,
    $6::NUMBER AS likes,
    $7::NUMBER AS comments,
    $8::TEXT AS duration
FROM 
    @YOUTUBE.RAW.MY_INTERNAL_STAGE/youtube_video_metrics.csv
    (FILE_FORMAT => 'YOUTUBE.RAW.VIDEO');

