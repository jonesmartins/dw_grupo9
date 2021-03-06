import pathlib

curr_dir = pathlib.Path(__file__).parent.resolve()

rootpath = pathlib.Path(f"{curr_dir}/../").resolve()

data_root_path = pathlib.Path(f"{rootpath}/data").resolve()

source_data_root_path = f"{data_root_path}/source_data"

database_root_path = f"{data_root_path}/covid_uk.sqlite"

schema_script_path = f"{rootpath}/database/database_schema.sql"

urls = {
    'table1.csv': 'https://api.coronavirus.data.gov.uk/v2/data?areaType=overview&metric=capacityPillarFour&metric=capacityPillarOneTwo&metric=capacityPillarThree&metric=hospitalCases&metric=covidOccupiedMVBeds&format=csv',
    'table2.csv': 'https://api.coronavirus.data.gov.uk/v2/data?areaType=overview&metric=newAdmissions&metric=newPeopleVaccinatedFirstDoseByPublishDate&metric=newVirusTests&metric=plannedCapacityByPublishDate&metric=newPeopleVaccinatedSecondDoseByPublishDate&format=csv'
}

source_data_csv = f"{source_data_root_path}/joined.csv"