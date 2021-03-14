create temp table _metric_ratings as
select distinct metric, rating, rating_description
from piura_region_of_peru_survey_data_scrubbing;

alter table _metric_ratings
    add primary key (metric, rating);

select *
from (select metric,
             sum(response * rating) / sum(response)::numeric rating,
             sum(response)
      from piura_region_of_peru_survey_data_scrubbing
      group by metric) x
         join _metric_ratings r on x.metric = r.metric
    and round(x.rating, 0) = r.rating;

alter table piura_region_of_peru_survey_data_scrubbing
    add column raw_value numeric;

update piura_region_of_peru_survey_data_scrubbing
set raw_value = replace(replace(raw_data,'%',''),'$','')::numeric
where raw_data <> 'Raw Data = Response Data'
  and response > 0;