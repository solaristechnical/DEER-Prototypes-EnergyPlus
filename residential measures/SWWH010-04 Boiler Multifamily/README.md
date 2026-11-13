# SWWH010-04 Central Boiler, Multifamily

This document describes the steps necessary to reproduce simulations and model outputs for the SWWH010-04 measure.

Prepared by Solaris Technical, Safia Sheerin - 2026-10-26

# Running simulations
``
cd /d "C:\DEER-Prototypes-EnergyPlus-SWWH010\residential measures\SWWH010-04 Boiler Multifamily\SWWH010 Boiler_MFm_Ex"
modelkit rake run

cd /d "C:\DEER-Prototypes-EnergyPlus-SWWH010\residential measures\SWWH010-04 Boiler Multifamily\SWWH010 Boiler_MFm_New"
modelkit rake run
``
# Post-processing
Run post-processing script.

Note: query.txt in the measure folder includes an additional parameter to the central boiler's nominal capacity for normalization.

ComponentSizingSummary/Entire Facility/Boiler:HotWater/Design Size Nominal Capacity/CENTRAL DHW DHW BOILER
```
cd /d "C:\DEER-Prototypes-EnergyPlus-SWWH010\residential measures\SWWH010-04 Boiler Multifamily"
python result3.py
```
Verify simdata.sqlite was created.

Export simdata to excel for energy savings calculations.
```
python export_simdata.py
```
Verfiy simdata_export.xlsx was created.

# Load shapes (not required for this measure)
If needed, run result.py in each sub folder (SWWH010 Boiler_MFm_Ex, SWWH010 Boiler_MFm_New)
``
python result.py
``
Verify results-sizing-agg.csv was created. Rename to results-summary.csv

Run measure-specific load shape scripts.
``
cd MEASURE FOLDER\residential measures\SWWH010-04 Boiler Multifamily
python MFm_SWWH010_Ex.py
python MFm_SWWH010_Ex.py
``