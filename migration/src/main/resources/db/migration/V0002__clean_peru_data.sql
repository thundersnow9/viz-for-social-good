create table piura_region_of_peru_survey_data_scrubbing as
select *
from piura_region_of_peru_survey_data;

create temp table _metric_descriptions as
select metric,
       sub_criteria,
       mode() within group ( order by metric_description ) metric_description
from piura_region_of_peru_survey_data
group by metric, sub_criteria;

update piura_region_of_peru_survey_data_scrubbing s
set metric_description = md.metric_description
from _metric_descriptions md
where s.metric = md.metric
  and s.sub_criteria = md.sub_criteria;

select metric, sub_criteria, count(distinct metric_description), count(*)
from piura_region_of_peru_survey_data_scrubbing
group by metric, sub_criteria;

create temp table _peru as
select category,
       criteria,
       sub_criteria,
       metric,
       metric_description,
       location,
       max(response_format)     response_format,
       max(raw_data)            raw_data,
       max(results_description) results_description,
       count(*)
from piura_region_of_peru_survey_data_scrubbing
group by category, criteria, sub_criteria, metric, metric_description, location;

update piura_region_of_peru_survey_data_scrubbing s
set response_format     = _peru.response_format,
    raw_data            = _peru.raw_data,
    results_description = _peru.results_description
from _peru
where _peru.category = s.category
  and _peru.criteria = s.criteria
  and _peru.sub_criteria = s.sub_criteria
  and _peru.metric = s.metric
  and _peru.metric_description = s.metric_description
  and _peru.location = s.location;