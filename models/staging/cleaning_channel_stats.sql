

with source as (
    select *
    from {{ source('YOUTUBE', 'YOUTUBE_CHANNEL_METRICS') }}
),

transformed as (
    select
        channel_id as ID,
        channel_title as Team,
        subscribers as Subscribers,
        total_views as No_Views,
        total_videos as No_Videos,
        country,
        
        -- Convert 'published_at' to Snowflake TIMESTAMP type
        try_to_timestamp_ntz(published_at) as published_at_ts,

        -- Split 'published_at' into date and time
        to_date(try_to_timestamp_ntz(published_at)) as published_date,
        to_char(try_to_timestamp_ntz(published_at), 'HH24:MI:SS') as published_time

    from source
)

select * from transformed
