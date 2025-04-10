CREATE OR REPLACE TABLE RAW.YOUTUBE_CHANNEL_METRICS AS
SELECT 
    $1::TEXT AS channel_id,
    $2::TEXT AS channel_title,
    $3::TEXT AS title,
    $4::TIMESTAMP_NTZ AS published_at,
    $5::NUMBER AS subscribers,
    $6::NUMBER AS total_views,
    $7::NUMBER AS total_videos,
    $8::TEXT AS country
FROM 
    @YOUTUBE.RAW.MY_INTERNAL_STAGE/youtube_CHANNEL_metrics.csv 
    (FILE_FORMAT => 'YOUTUBE.RAW.CHANNEL');  
