import pandas as pd
from pathlib import Path

# CSV files
csv_files = [
    # MFm Ex
    Path(r"C:\Projects\SWHC027-09\residential measures\SWHC027-09 PTAC PTHP\SWHC027-09 PTAC PTHP_MFm_Ex\cases\MFm&0&rPTAC&Ex&dxAC_equip__pkgTerm.csv"),
    # MFm New
    Path(r"C:\Projects\SWHC027-09\residential measures\SWHC027-09 PTAC PTHP\SWHC027-09 PTAC PTHP_MFm_New\cases\MFm&0&rPTAC&New&dxAC_equip__pkgTerm.csv"),
    # SFm 1975
    Path(r"C:\Projects\SWHC027-09\residential measures\SWHC027-09 PTAC PTHP\SWHC027-09 PTAC PTHP_SFm_1975\cases\SFm&1&rPTAC&Ex&dxAC_equip__pkgTerm.csv"),
    Path(r"C:\Projects\SWHC027-09\residential measures\SWHC027-09 PTAC PTHP\SWHC027-09 PTAC PTHP_SFm_1975\cases\SFm&2&rPTAC&Ex&dxAC_equip__pkgTerm.csv"),
    # SFm 1985
    Path(r"C:\Projects\SWHC027-09\residential measures\SWHC027-09 PTAC PTHP\SWHC027-09 PTAC PTHP_SFm_1985\cases\SFm&1&rPTAC&Ex&dxAC_equip__pkgTerm.csv"),
    Path(r"C:\Projects\SWHC027-09\residential measures\SWHC027-09 PTAC PTHP\SWHC027-09 PTAC PTHP_SFm_1985\cases\SFm&2&rPTAC&Ex&dxAC_equip__pkgTerm.csv"),
    # SFm New
    Path(r"C:\Projects\SWHC027-09\residential measures\SWHC027-09 PTAC PTHP\SWHC027-09 PTAC PTHP_SFm_New\cases\SFm&1&rPTAC&New&dxAC_equip__pkgTerm.csv"),
    Path(r"C:\Projects\SWHC027-09\residential measures\SWHC027-09 PTAC PTHP\SWHC027-09 PTAC PTHP_SFm_New\cases\SFm&2&rPTAC&New&dxAC_equip__pkgTerm.csv")
]


# Same values will be pasted into EVERY CSV
case_names = [
    "NE-dxAC_equip-pkgTerm-EER-9.41-Std",
    "NE-dxAC_equip-pkgTerm-EER-8.56-Std",
    "NE-dxAC_equip-pkgTerm-EER-7.71-Std",
    "NE-dxAC_equip-pkgTerm-EER-11.9-Std",
    "NE-dxAC_equip-pkgTerm-EER-10.70-Std",
    "NE-dxAC_equip-pkgTerm-EER-9.5-Std",
    "NE-dxAC_equip-pkgTerm-EER-10.35-Msr",
    "NE-dxAC_equip-pkgTerm-EER-9.42-Msr",
    "NE-dxAC_equip-pkgTerm-EER-8.48-Msr",
    "NE-dxAC_equip-pkgTerm-EER-13.09-Msr",
    "NE-dxAC_equip-pkgTerm-EER-11.77-Msr",
    "NE-dxAC_equip-pkgTerm-EER-10.45-Msr"
]

cool_cops = [
    3.19, 
    2.90, 
    2.61, 
    4.03, 
    3.63, 
    3.22, 
    3.50, 
    3.19, 
    2.88, 
    4.43, 
    3.99, 
    3.54 
]

required_columns = [
    "case_name",
    ":main_cool_coil_cop"
]


for filepath in csv_files:

    print(f"Processing: {filepath}")

    df = pd.read_csv(filepath)

    # Check required columns
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(
                f"{filepath}: column '{col}' was not found."
            )

    # Check that the number of rows matches your lists
    if not (
        len(df) == len(case_names)
        == len(cool_cops)
    ):
        raise ValueError(
            f"{filepath} has {len(df)} rows, but the replacement "
            f"lists have {len(case_names)} values."
        )

    # Replace the three columns in order
    df["case_name"] = case_names
    df[":main_cool_coil_cop"] = cool_cops

    # Save over original file
    df.to_csv(filepath, index=False)

    print("  Updated successfully")

print("All files complete.")