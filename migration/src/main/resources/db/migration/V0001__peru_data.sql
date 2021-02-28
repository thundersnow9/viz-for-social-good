create table if not exists piura_region_of_peru_survey_data
(
    category            text,
    criteria            text,
    sub_criteria        text,
    metric              text,
    metric_description  text,
    location            text,
    rating              int,
    rating_description  text,
    response            int,
    response_format     text,
    raw_data            text,
    results_description text
);

/*
   \copy piura_region_of_peru_survey_data
   from 'migration/src/main/resources/data/Piura-Region-of-Peru-Survey-Data-for-Viz.csv'
   delimiter ','
   csv header;
 */