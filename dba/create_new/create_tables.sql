-- Lookup Tables
CREATE TABLE public.region_lk
(
  region_code smallint PRIMARY KEY,
  region_name character varying(50),
  region_desc character varying(100)
);

CREATE TABLE state_lk (
state_id int PRIMARY KEY,
STATE_ABBR character(2),
STATE_NAME varchar(50),
STATE_FIPS_CODE int,
region_code smallint REFERENCES region_lk(region_code)
);

CREATE TABLE table_key_mapping (
  uuid serial  PRIMARY KEY,
  table_name varchar(50),
  column_name varchar(50),
  key varchar(50),
  ui_component varchar(50),
  title varchar(150),
  category varchar(150),
  noun varchar(50),
  short_title varchar(50)
);

CREATE TABLE nibrs_victim_count (
    data_year int,
    state_id int,
    state_abbr character(2),
    agency_id int,
    ori varchar(50),
    offense_name varchar(50),
    victim_type_name varchar(50),
    sex_code character(1),
    age_range varchar(50),
    race_desc varchar(50),
    ethnicity_name varchar(50),
    location varchar(100),
    count int
);


CREATE TABLE nibrs_offender_count (
    data_year int,
    state_id int,
    state_abbr character(2),
    agency_id int,
    ori varchar(50),
    offense_name varchar(50),
    sex_code character(1),
    race_desc varchar(50),
    ethnicity_name varchar(50),
    age_range varchar(50),
    count int
);


CREATE TABLE nibrs_victim_to_offender_relationship_count (
    data_year int,
    state_id int,
    state_abbr character(2),
    agency_id int,
    ori varchar(50),
    offense_name varchar(50),
    relationship varchar(50),
    count int
);

CREATE TABLE nibrs_offense_count (
    data_year int,
    state_id int,
    state_abbr character(2),
    agency_id int,
    ori varchar(50),
    offense_name varchar(50),
    incident_count int,
    offense_count int
);


-- LEOKA Tables
CREATE TABLE public.leoka_assault_data
(
  DATA_YEAR INT,
  AGENCY_ID INT,
  ORI VARCHAR(25),
  MONTH_NUM INT,
  LKASUM_MOTH_ID INT,
  MONTH_PUB_STATUS INT,
  STATE_ID INT,
  STATE_ABBR VARCHAR(2),
  DIVISION_CODE INT,
  DIVISION_NAME VARCHAR(100),
  REGION_CODE INT,
  REGION_NAME VARCHAR(100),
  ACTIVITY_ID INT,
  ACTIVITY_NAME VARCHAR(100),
  TWO_OFFICER_VEHICLE_ACTUAL INT,
  ONE_OFFICER_VEHICLE_ACTUAL INT,
  ONE_OFFICER_ASSISTED_ACTUAL INT,
  DET_SPE_ASS_ALONE_ACTUAL INT,
  DET_SPE_ASS_ASSISTED_ACTUAL INT,
  OTHER_ALONE_ACTUAL INT,
  OTHER_ASSISTED_ACTUAL INT,
  FIREARM_ACTUAL INT,
  KNIFE_ACTUAL INT,
  HANDS_FISTS_FEET_ACTUAL INT,
  OTHER_ACTUAL INT,
  CLEARED_COUNT INT
);


-- Agency Data
CREATE TABLE public.agency_data
(
  YEARLY_AGENCY_ID int,
  AGENCY_ID int,
  DATA_YEAR int,
  ORI varchar(25),
  LEGACY_ORI varchar(25),
  COVERED_BY_LEGACY_ORI varchar(25),
  DIRECT_CONTRIBUTOR_FLAG varchar(1),
  DORMANT_FLAG varchar(1),
  DORMANT_YEAR int,
  REPORTING_TYPE varchar(1),
  UCR_AGENCY_NAME varchar(100),
  NCIC_AGENCY_NAME varchar(100),
  PUB_AGENCY_NAME varchar(100),
  PUB_AGENCY_UNIT varchar(100),
  AGENCY_STATUS varchar(1),
  STATE_ID int,
  STATE_NAME varchar(100),
  STATE_ABBR varchar(2),
  STATE_POSTAL_ABBR varchar(2),
  DIVISION_CODE int,
  DIVISION_NAME varchar(100),
  REGION_CODE int,
  REGION_NAME varchar(100),
  REGION_DESC varchar(100),
  AGENCY_TYPE_NAME varchar(100),
  POPULATION int,
  SUBMITTING_AGENCY_ID int,
  SAI varchar(25),
  SUBMITTING_AGENCY_NAME varchar(200),
  SUBURBAN_AREA_FLAG varchar(1),
  POPULATION_GROUP_ID int,
  POPULATION_GROUP_CODE varchar(2),
  POPULATION_GROUP_DESC varchar(100),
  PARENT_POP_GROUP_CODE int,
  PARENT_POP_GROUP_DESC varchar(100),
  MIP_FLAG varchar(1),
  POP_SORT_ORDER int,
  SUMMARY_RAPE_DEF varchar(1),
  PE_REPORTED_FLAG varchar(1),
  PE_OFFICER_COUNT int,
  PE_CIVILIAN_COUNT int,
  MALE_OFFICER int,
  MALE_CIVILIAN int,
  MALE_TOTAL int,
  FEMALE_OFFICER int,
  FEMALE_CIVILIAN int,
  FEMALE_TOTAL int,
  OFFICER_RATE int,
  EMPLOYEE_RATE int,
  NIBRS_CERT_DATE date,
  NIBRS_START_DATE date,
  NIBRS_LEOKA_START_DATE date,
  NIBRS_CT_START_DATE date,
  NIBRS_MULTI_BIAS_START_DATE date,
  NIBRS_OFF_ETH_START_DATE date,
  COVERED_FLAG varchar(1),
  COUNTY_NAME varchar(100),
  MSA_NAME varchar(100),
  PUBLISHABLE_FLAG varchar(1)
);

-- RETA data
CREATE TABLE public.summarized_data
(
	DATA_YEAR	smallint,
	AGENCY_ID	int,
	MONTH_NUM	smallint,
	ori varchar(25),
	SUM_UNKNOWN_ACTUAL int,
	SUM_UNKNOWN_CLEARED int,
	SUM_UNKNOWN_JUV_CLEARED int,
	SUM_HOM_ACTUAL int,
	SUM_HOM_CLEARED int,
	SUM_HOM_JUV_CLEARED int,
	SUM_MAN_ACTUAL int,
	SUM_MAN_CLEARED int,
	SUM_MAN_JUV_CLEARED int,
	SUM_RPE_NS_LEG_ACTUAL int,
	SUM_RPE_NS_LEG_CLEARED int,
	SUM_RPE_NS_LEG_JUV_CLEARED int,
	SUM_RPE_FRC_LEG_ACTUAL int,
	SUM_RPE_FRC_LEG_CLEARED int,
	SUM_RPE_FRC_LEG_JUV_CLEARED int,
	SUM_RPE_ATT_LEG_ACTUAL int,
	SUM_RPE_ATT_LEG_CLEARED int,
	SUM_RPE_ATT_LEG_JUV_CLEARED int,
	SUM_RPE_NS_ACTUAL int,
	SUM_RPE_NS_CLEARED int,
	SUM_RPE_NS_JUV_CLEARED int,
	SUM_RPE_FRC_ACTUAL int,
	SUM_RPE_FRC_CLEARED int,
	SUM_RPE_FRC_JUV_CLEARED int,
	SUM_RPE_ATT_ACTUAL int,
	SUM_RPE_ATT_CLEARED int,
	SUM_RPE_ATT_JUV_CLEARED int,
	SUM_ROB_NS_ACTUAL int,
	SUM_ROB_NS_CLEARED int,
	SUM_ROB_NS_JUV_CLEARED int,
	SUM_ROB_GUN_ACTUAL int,
	SUM_ROB_GUN_CLEARED  int,
	SUM_ROB_GUN_JUV_CLEARED int,
	SUM_ROB_CUT_ACTUAL int,
	SUM_ROB_CUT_CLEARED int,
	SUM_ROB_CUT_JUV_CLEARED int,
	SUM_ROB_OTH_ACTUAL int,
	SUM_ROB_OTH_CLEARED int,
	SUM_ROB_OTH_JUV_CLEARED int,
	SUM_ROB_HFF_ACTUAL int,
	SUM_ROB_HFF_CLEARED int,
	SUM_ROB_HFF_JUV_CLEARED int,
	SUM_ASS_NS_ACTUAL int,
	SUM_ASS_NS_CLEARED int,
	SUM_ASS_NS_JUV_CLEARED int,
	SUM_ASS_GUN_ACTUAL int,
	SUM_ASS_GUN_CLEARED int,
	SUM_ASS_GUN_JUV_CLEARED int,
	SUM_ASS_CUT_ACTUAL int,
	SUM_ASS_CUT_CLEARED int,
	SUM_ASS_CUT_JUV_CLEARED int,
	SUM_ASS_OTH_ACTUAL int,
	SUM_ASS_OTH_CLEARED int,
	SUM_ASS_OTH_JUV_CLEARED int,
	SUM_ASS_HFF_ACTUAL int,
	SUM_ASS_HFF_CLEARED int,
	SUM_ASS_HFF_JUV_CLEARED int,
	SUM_ASS_SMP_ACTUAL int,
	SUM_ASS_SMP_CLEARED int,
	SUM_ASS_SMP_JUV_CLEARED int,
	SUM_BRG_NS_ACTUAL int,
	SUM_BRG_NS_CLEARED int,
	SUM_BRG_NS_JUV_CLEARED int,
	SUM_BRG_FEO_ACTUAL int,
	SUM_BRG_FEO_CLEARED int,
	SUM_BRG_FEO_JUV_CLEARED int,
	SUM_BRG_UEO_ACTUAL int,
	SUM_BRG_UEO_CLEARED int,
	SUM_BRG_UEO_JUV_CLEARED int,
	SUM_BRG_AFE_ACTUAL int,
	SUM_BRG_AFE_CLEARED int,
	SUM_BRG_AFE_JUV_CLEARED int,
	SUM_LAR_TFT_ACTUAL int,
	SUM_LAR_TFT_CLEARED int,
	SUM_LAR_TFT_JUV_CLEARED int,
	SUM_MTR_NS_ACTUAL int,
	SUM_MTR_NS_CLEARED int,
	SUM_MTR_NS_JUV_CLEARED int,
	SUM_MTR_ATO_ACTUAL int,
	SUM_MTR_ATO_CLEARED int,
	SUM_MTR_ATO_JUV_CLEARED int,
	SUM_MTR_TRK_ACTUAL int,
	SUM_MTR_TRK_CLEARED int,
	SUM_MTR_TRK_JUV_CLEARED int,
	SUM_MTR_OTH_ACTUAL int,
	SUM_MTR_OTH_CLEARED int,
	SUM_MTR_OTH_JUV_CLEARED int,
	SUM_HT_NS_ACTUAL int,
	SUM_HT_NS_CLEARED int,
	SUM_HT_NS_JUV_CLEARED int,
	SUM_HT_SEX_ACTUAL int,
	SUM_HT_SEX_CLEARED int,
	SUM_HT_SEX_JUV_CLEARED int,
	SUM_HT_SRV_ACTUAL int,
	SUM_HT_SRV_CLEARED int,
	SUM_HT_SRV_JUV_CLEARED int,
	SUM_ARS_ACTUAL int,
	SUM_ARS_CLEARED int,
	SUM_ARS_JUV_CLEARED int
);
