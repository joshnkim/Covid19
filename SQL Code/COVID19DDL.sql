CREATE TABLE hhs_hospitalizations_raw (
	state VARCHAR(2),
    date DATE,
    previous_day_admission_adult_covid_confirmed INT,
    total_adult_patients_hospitalized_confirmed_covid	INT,
    total_pediatric_patients_hospitalized_confirmed_covid	INT, 
    inpatient_beds_utilization	FLOAT,
    inpatient_bed_covid_utilization	FLOAT,
    adult_icu_bed_covid_utilization	FLOAT,
    deaths_covid	INT,
    previous_day_admission_pediatric_covid_confirmed_0_4	INT,
    previous_day_admission_pediatric_covid_confirmed_12_17	INT,
    previous_day_admission_pediatric_covid_confirmed_5_11	INT,
    previous_day_admission_pediatric_covid_confirmed_unknown	INT
    );
    

DROP TABLE IF EXISTS cdc_vaccinations_raw;

    CREATE TABLE cdc_vaccinations_raw (
		Date VARCHAR(20),
        MMWR_week	INT,
        Location	VARCHAR(2),
        Administered_Dose1_Recip	INT,
        Administered_Dose1_Pop_Pct	FLOAT,
        Series_Complete_Yes	INT,
        Series_Complete_Pop_Pct	FLOAT,
        Additional_Doses	INT,
        Additional_Doses_Vax_Pct	FLOAT
        );


        

        
        
	LOAD DATA LOCAL INFILE '/Users/jush/Downloads/COVID-19_Reported_Patient_Impact_and_Hospital_Capacity_by_State_Timeseries__RAW_.csv'
        INTO TABLE hhs_hospitalizations_raw 
        FIELDS TERMINATED BY ','
        LINES TERMINATED BY '\n'
        IGNORE 1 ROWS 
        (
			state,
			date,
			previous_day_admission_adult_covid_confirmed,
			total_adult_patients_hospitalized_confirmed_covid,
			total_pediatric_patients_hospitalized_confirmed_covid, 
			inpatient_beds_utilization,
			inpatient_bed_covid_utilization,
			adult_icu_bed_covid_utilization,
			deaths_covid,
			previous_day_admission_pediatric_covid_confirmed_0_4,
			previous_day_admission_pediatric_covid_confirmed_12_17	,
			previous_day_admission_pediatric_covid_confirmed_5_11,
			previous_day_admission_pediatric_covid_confirmed_unknown
            );
            
            
SELECT DATE_FORMAT(date, '%m/%d/%y') AS 'Date'
FROM  hhs_hospitalizations_raw;
            
            
            
LOAD DATA LOCAL INFILE '/Users/jush/Downloads/vax_data_cleaned.csv'
INTO TABLE cdc_vaccinations_raw
FIELDS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
    Date,
    MMWR_week,
    Location,
    Administered_Dose1_Recip,
    Administered_Dose1_Pop_Pct,
    Series_Complete_Yes,
    Series_Complete_Pop_Pct,
    Additional_Doses,
    Additional_Doses_Vax_Pct
);


UPDATE cdc_vaccinations_raw
SET Date = STR_TO_DATE(Date, '%m/%d/%Y');


-- DROP VIEW IF EXISTS covid_master_table;
CREATE VIEW covid_master_table AS 
SELECT 
			h.state,
			h.date,
			h.previous_day_admission_adult_covid_confirmed,
			h.total_adult_patients_hospitalized_confirmed_covid,
			h.total_pediatric_patients_hospitalized_confirmed_covid, 
			h.inpatient_beds_utilization,
			h.inpatient_bed_covid_utilization,
			h.adult_icu_bed_covid_utilization,
			h.deaths_covid,
			(
				h.previous_day_admission_pediatric_covid_confirmed_0_4 + 
                h.previous_day_admission_pediatric_covid_confirmed_12_17	+ 
                h.previous_day_admission_pediatric_covid_confirmed_5_11 +
                h.previous_day_admission_pediatric_covid_confirmed_unknown
			) AS pediatric_covid_confirmed, 
			v.MMWR_week,
			v.Administered_Dose1_Recip,
			v.Administered_Dose1_Pop_Pct,
			v.Series_Complete_Yes,
			v.Series_Complete_Pop_Pct,
			v.Additional_Doses,
			v.Additional_Doses_Vax_Pct
	FROM hhs_hospitalizations_raw h
    JOIN cdc_vaccinations_raw v
    ON h.state = v.Location
    AND h.date = v.Date;
    
    
    
    
    
    DESC  hhs_hospitalizations_raw;
	DESC cdc_vaccinations_raw;
    
    

    SELECT * FROM hhs_hospitalizations_raw;
    SELECT * FROM cdc_vaccinations_raw;
	SELECT * FROM covid_master_table;
    


CREATE TABLE antivax_sentiment_raw (
County_Name VARCHAR(55),
State VARCHAR(2),
Estimated_hesitant FLOAT,
Estimated_hesitant_or_unsure FLOAT,
Estimated_strongly_hesitant FLOAT,
Percent_adults_fully_vaccinated_against_COVID19_2021 FLOAT
);

LOAD DATA LOCAL INFILE '/Users/jush/Downloads/antivax_cleaned.csv'
    INTO TABLE antivax_sentiment_raw
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS;
    
    
    SELECT * FROM antivax_sentiment_raw
    ORDER BY State;
    
CREATE TABLE state_politics_raw (
State VARCHAR(2),
Dem_or_rep VARCHAR(10)
);

LOAD DATA LOCAL INFILE '/Users/jush/Downloads/state_politics.csv'
	INTO TABLE state_politics_raw 
	FIELDS TERMINATED BY ','
	OPTIONALLY ENCLOSED BY '"'
	LINES TERMINATED BY '\n'
	IGNORE 1 ROWS;
    
SELECT * FROM state_politics_raw;


CREATE TABLE population_raw (
NAME VARCHAR(2),
POPESTIMATE2021 INT,
DEATHS2021 int
);

LOAD DATA LOCAL INFILE '/Users/jush/Downloads/populations_cleaned.csv'
    INTO TABLE population_raw
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS;



SELECT * FROM population_raw;