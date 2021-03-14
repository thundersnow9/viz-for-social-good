import pandas as pd
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('postgresql://merrowa@localhost:5435/merrowa')  # uses password from .pgpass

    household_hygiene = pd.read_excel('JMP_2019_WLD.xlsx', sheet_name='Hygiene Data')
    household_sanitation = pd.read_excel('JMP_2019_WLD.xlsx', sheet_name='Sanitation Data')
    household_water = pd.read_excel('JMP_2019_WLD.xlsx', sheet_name='Water Data')

    school_hygiene = pd.read_excel('JMP_2020_WinS_WLD.xlsx', sheet_name='Hygiene Data')
    school_sanitation = pd.read_excel('JMP_2020_WinS_WLD.xlsx', sheet_name='Sanitation Data')
    school_water = pd.read_excel('JMP_2020_WinS_WLD.xlsx', sheet_name='Water Data')

    regions = pd.read_excel('JMP_2020_WinS_WLD.xlsx', sheet_name='Regions')

    healthcare_facilities_hygiene = pd.read_excel('JMP_2020_WinHCF_WLD.xlsx', sheet_name='hyg')
    healthcare_facilities_sanitation = pd.read_excel('JMP_2020_WinHCF_WLD.xlsx', sheet_name='san')
    healthcare_facilities_water = pd.read_excel('JMP_2020_WinHCF_WLD.xlsx', sheet_name='wat')
    healthcare_facilities_waste_mgmt = pd.read_excel('JMP_2020_WinHCF_WLD.xlsx', sheet_name='wman')
    healthcare_facilities_cleaning = pd.read_excel('JMP_2020_WinHCF_WLD.xlsx', sheet_name='clean')

    long_names = {
        'pop': 'population',
        'prop': 'pct',
        'u': 'urban',
        'n': 'national',
        'r': 'rural',
        'hyg': 'hygiene',
        'bas': 'basic',
        'lim': 'limited',
        'nfac': 'no facility',
        'san': 'sanitation',
        'wat': 'water',
        'unimp': 'unimproved',
        'arc': 'annual rate of change',
        'sur': 'surface',
        'sm': 'safely managed',
        'pip': 'piped',
        'npip': 'non-piped',
        'premises': 'accessible on premises',
        'available': 'available when needed',
        'quality': 'free from comtamination',
        'schoolagepop': 'school age population in thousands',
        'nat': 'national',
        'urb': 'urban',
        'pre': 'pre primary',
        'pri': 'primary',
        'sec': 'secondary',
        'poc': 'handwashing facilities at points of care',
        'toi': 'handwashing facilities near toilets',
        'imp': 'improved',
        'ius': 'improved and usable',
        'imop': 'improved on premises',
        'wman': 'waste management',
        'seg': 'waste segregated',
        'trd': 'waste treated',
        'pro': 'protocols for cleaning',
        'trn': 'training on cleaning'
    }

    data = [household_hygiene,
            household_sanitation,
            household_water,
            school_hygiene,
            school_sanitation,
            school_water,
            regions,
            healthcare_facilities_hygiene,
            healthcare_facilities_sanitation,
            healthcare_facilities_water,
            healthcare_facilities_waste_mgmt,
            healthcare_facilities_cleaning]


    def expand_column_name(name):
        expanded_name = ''
        split = name.split('_')
        for n in split:
            if n in long_names.keys():
                expanded_name += long_names[n]
            else:
                expanded_name += n
            expanded_name += ' '

        return expanded_name.title().strip()


    for df in data:
        df.rename({k: expand_column_name(k) for k in df.keys()}, axis='columns', inplace=True)

    household_hygiene.to_sql(name='household_hygiene', con=engine, if_exists='replace')
    household_sanitation.to_sql(name='household_sanitation', con=engine, if_exists='replace')
    household_water.to_sql(name='household_water', con=engine, if_exists='replace')
    school_hygiene.to_sql(name='school_hygiene', con=engine, if_exists='replace')
    school_sanitation.to_sql(name='school_sanitation', con=engine, if_exists='replace')
    school_water.to_sql(name='school_water', con=engine, if_exists='replace')
    regions.to_sql(name='regions', con=engine, if_exists='replace')
    healthcare_facilities_hygiene.to_sql(name='healthcare_facilities_hygiene', con=engine, if_exists='replace')
    healthcare_facilities_sanitation.to_sql(name='healthcare_facilities_sanitation', con=engine, if_exists='replace')
    healthcare_facilities_water.to_sql(name='healthcare_facilities_water', con=engine, if_exists='replace')
    healthcare_facilities_waste_mgmt.to_sql(name='healthcare_facilities_waste_mgmt', con=engine, if_exists='replace')
    healthcare_facilities_cleaning.to_sql(name='healthcare_facilities_cleaning', con=engine, if_exists='replace')
