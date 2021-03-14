create or replace view tapwater_for_tableau as
select hh."Iso3"                              "ISO-3",
       hh."Name",
       "Year",
       'National'                             "Segment",
       (hh."Population National" * 1000)::int "Population",
       hh."Water Basic National"              "Water Basic",
       100 - "Water Basic National"           "Water Substandard"
from household_water hh

union all

select hh."Iso3"                                                               "ISO-3",
       hh."Name",
       "Year",
       'Rural'                                                                 "Segment",
       ((1 - (hh."Pct Urban" / 100)) * (hh."Population National" * 1000))::int "Population",
       hh."Water Basic Rural"                                                  "Water Basic",
       100 - "Water Basic Rural"                                               "Water Substandard"
from household_water hh

union all

select hh."Iso3"                                                         "ISO-3",
       hh."Name",
       "Year",
       'Urban'                                                           "Segment",
       ((hh."Pct Urban" / 100) * (hh."Population National" * 1000))::int "Population",
       hh."Water Basic Urban"                                            "Water Basic",
       100 - "Water Basic Urban"                                         "Water Substandard"
from household_water hh;