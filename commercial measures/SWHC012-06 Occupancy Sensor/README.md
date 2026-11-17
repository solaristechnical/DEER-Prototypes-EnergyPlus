# SWHC012-06 Occupancy Sensor, Classroom

## Measure Description

This folder contains the commercial Occupancy Sensor measure setup used for DEER prototype simulation, result scraping, andd ownstream post-processing.

## Key Changes in This Revision
- Updated to CZ2025 weather files
- Updated sizing map 22-2 to accomodate Pump:VariableSpeed (breaking change from main branch)
- Reverted interim workaround (old version of prototypes)
- For generated schedules, use calendar year 2009 (start day = Thursday)
- Added lines to Com.py to deal with hardsize instance files
- Removed DXGF case for ERC and DXHP for EPr and ESe to align with eTRM offerings

### Cohorts and Cases

| Case Name (TechID) | Case Type |Building Type | Building Vintage |
|-------------------|-------|------|--------|
| NE-HV_Tech-OccSens-cDXGF-NoOccSens | Base Case| EPr, ESe | Ex, New |
| NE-HV_Tech-OccSens-cDXHP-NoOccSens | Base Case | ERC | Ex, New |
| NE-HV_Tech-OccSens-cDXGF | Measure Case| EPr, ESe | Ex, New |
| NE-HV_Tech-OccSens-cDXHP | Measure Case| ERC | Ex, New |

### HVAC-Zone Template

Providing a filename via the parameter classroom_class_setpoint_temp_schedule parameter triggers the prototypes to read in a temperature setpoint schedule from file. The filename is specified in the hvac-zone template using a relative path to its location in the measure folder.

**templates\energyplus\templates\zonehvac\hvac-zone.pxt near line 590**

```
  Schedule:File,
	<%=zone_name %> Cooling Setpoint Schedule,  !- Name
    Temperature,             !- Schedule Type Limits Name
	C:/DEER-Prototypes-EnergyPlus/commercial measures/SWHC012-05 Occupancy Sensor/<%= setpoint_temp_schedule %>,  !- File Name
    3,                       !- Column Number
    1,                       !- Rows to Skip at Top
    8760,                    !- Number of Hours of Data
    Comma,                   !- Column Separator
    No,                      !- Interpolate to Timestep
    10,                      !- Minutes per Item
    Yes;                     !- Adjust Schedule for Daylight Savings
```
**templates\energyplus\templates\zonehvac\hvac-zone.pxt near line 612**

```
  Schedule:File,
	<%=zone_name %> Heating Setpoint Schedule,  !- Name
    Temperature,             !- Schedule Type Limits Name
	C:/DEER-Prototypes-EnergyPlus/commercial measures/SWHC012-05 Occupancy Sensor/<%= setpoint_temp_schedule %>,  !- File Name
    4,                       !- Column Number
    1,                       !- Rows to Skip at Top
    8760,                    !- Number of Hours of Data
    Comma,                   !- Column Separator
    No,                      !- Interpolate to Timestep
    10,                      !- Minutes per Item
    Yes;                     !- Adjust Schedule for Daylight Savings
```

## Simulation and Post-Processing
- Copy `22-2.csv` from the **sizing-map** folder into **C:\Program Files (x86)\Modelkit Caboodle\lib\rubygems\gems\modelkit-energyplus-0.3.0\resources\sizing-map**
- Run `schedule.py` to generate schedules for each building type
- Run simulations and confirm result files
- Scrape energy usage outputs with `scripts/result2.py` using `query_SWHC012.txt` (see below for more details)
- Extract normalizing units with `result2.py` and `result_filtered.py` using `query_SWHC012_normalizing.txt` (see below for more details)
- Run transformation script `Com.py` from **scripts/data transformation**
- Review result files: `simdata.csv`, `sizing_agg_filtered.csv`, `CEDARS_LoadShape_Com.zip`

### Extracting Energy Usages
The file `query_SWHC012.txt` includes queries for energy usages. To extract the energy usages after running simulations, enter the following commands: 
```
cd 'C:/DEER-Prototypes/commercial measures/SWHC012-06 Occupancy Sensor'
python result2.py -q query_SWHC012.txt
```

### Extracting Normalizing Units
The file `query_SWHC012_normalizing.txt` Developers applied the measure to only those zones representing classrooms, taken to mean where zone_type prefix is *classroom_class*. Developers considered area (from zones), cooling capacity (from cooling coils), and cooling capacity (from AirLoopHVAC systems) as candidates for normalizing units, ultimately choosing cooling capacity from AirLoopHVAC systems.

The total cooling capacity of classroom zones in a given building simulation is calculated using a multi-step process to tabulate cooling capacity for each system in the model and then filter relevant systems and aggregate the capacity of matching systems.

To extract the cooling capacity normalizing units, use the following steps:

1. Change directory into the **Ex** vintage subfolder and run the data extraction script with commands:
   ```
   cd 'C:/DEER-Prototypes-EnergyPlus/commercial measures/SWHC012-06 Occupancy Sensor/SWHC012-06 Occupancy Sensor_Ex'
   python ../result2.py -s -t -q ../query_SWHC012_normalizing.txt
   ```
   At this point, the user should have a new SQLite file `simdata.sqlite` saved by the script with tables sim_metadata and sim_tabular, which contains cooling capacity figures for each building instance and system.

2. Continue with the command to reformat sizing data:
   ```
   cat ../extract_sizing_data_sqlite.sql | sqlite3 simdata.sqlite -csv -header > results-sizing-detail.csv
   ```
   At this point, the user should have a new file `results-sizing-detail.csv` in the database.

3. Export `results-sizing-detail.csv` from the database to the **Ex** vintage subfolder.

4. Repeat Steps 1 through 3 for the **New** vintage subfolder.

5. Change to the parent directory and continue with the command to filter the sizing results:
   ```
   cd 'C:/DEER-Prototypes-EnergyPlus/commercial measures/SWHC012-06 Occupancy Sensor'
   python result_filtered.py
   ```
   The result_filtered script cross-references the `results-sizing-detail.csv` and `coil_list.xlsx` in order to filter relevant zones or systems. At this point, the user should have a new file `sizing_agg_filtered.csv` in each vintage subfolder.

6. Combine the `sizing_agg_filtered.csv` files into one CSV file and archive with the energy model outputs. The combined file contains the full normalizing unit lookup table, which is used in the energy savings calculation workbook.

### Classroom System Names
The classroom system names were manually identified by inspection of prototype root files and tabulated in the file `coil_list.xlsx` (sheet "Main coils").

### Data Transformation and Post-Processing
Measure Working List: `DEER_EnergyPlus_Modelkit_Measure_list_working_SWHC012-06.xlsx`

### Load Shape Workaround
The load shape files (located in `CEDARS_LoadShape_Com.zip`) are missing the normalizing unit column required for uploading to CEDARS. Use the following steps to update the load shape files:
1. Unzip `CEDARS_LoadShape_Com.zip`.
2. Open `CEDARS_LoadShape_Com_EPr.csv`.
3. Add a column between 'BldgLoc' and 'Type (Whole Building or End Use)' called  'NormUnit'.
4. Enter the value 'Cap-Tons' for all subsequent lines.
5. Repeat Steps 2 through 4 for the other building type files (labeled `ERC` and `ESe`).
6. Rezip the 3 edited files as `CEDARS_LoadShape_Com.zip`.

### Occupancy Schedule
`OccSchedule vs TempSetpointSch.xlsx` shows details of the occupancy schedule and assigned temperature setpoints based on classroom usage, days of the week, and holidays.
