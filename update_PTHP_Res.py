import pandas as pd
from pathlib import Path

# CSV files
csv_files = [
    # MFm Ex
    Path(r"C:\Projects\dev-SWHC027-09\residential measures\SWHC027-09 PTAC PTHP\SWHC027-09 PTAC PTHP_MFm_Ex\cases\MFm&0&rPTHP&Ex&dxHP_equip__pkgTerm.csv"),
    # MFm New
    Path(r"C:\Projects\dev-SWHC027-09\residential measures\SWHC027-09 PTAC PTHP\SWHC027-09 PTAC PTHP_MFm_New\cases\MFm&0&rPTHP&New&dxHP_equip__pkgTerm.csv"),
    # SFm 1975
    Path(r"C:\Projects\dev-SWHC027-09\residential measures\SWHC027-09 PTAC PTHP\SWHC027-09 PTAC PTHP_SFm_1975\cases\SFm&1&rPTHP&Ex&dxHP_equip__pkgTerm.csv"),
    Path(r"C:\Projects\dev-SWHC027-09\residential measures\SWHC027-09 PTAC PTHP\SWHC027-09 PTAC PTHP_SFm_1975\cases\SFm&2&rPTHP&Ex&dxHP_equip__pkgTerm.csv"),
    # SFm 1985
    Path(r"C:\Projects\dev-SWHC027-09\residential measures\SWHC027-09 PTAC PTHP\SWHC027-09 PTAC PTHP_SFm_1985\cases\SFm&1&rPTHP&Ex&dxHP_equip__pkgTerm.csv"),
    Path(r"C:\Projects\dev-SWHC027-09\residential measures\SWHC027-09 PTAC PTHP\SWHC027-09 PTAC PTHP_SFm_1985\cases\SFm&2&rPTHP&Ex&dxHP_equip__pkgTerm.csv"),
    # SFm New
    Path(r"C:\Projects\dev-SWHC027-09\residential measures\SWHC027-09 PTAC PTHP\SWHC027-09 PTAC PTHP_SFm_New\cases\SFm&1&rPTHP&New&dxHP_equip__pkgTerm.csv"),
    Path(r"C:\Projects\dev-SWHC027-09\residential measures\SWHC027-09 PTAC PTHP\SWHC027-09 PTAC PTHP_SFm_New\cases\SFm&2&rPTHP&New&dxHP_equip__pkgTerm.csv")
]

case_names_new = [
    "RE-HV-PTHP-10.70EER-3.13COP",
    "RE-HV-PTHP-11.77EER-3.44COP"
]

case_names_ex = [
    "RE-HV-PTHP-8.46EER-2.61COP",
    "RE-HV-PTHP-9.31EER-2.87COP",
    "RE-HV-PTHP-10.70EER-3.13COP",
    "RE-HV-PTHP-11.77EER-3.44COP"
]

cool_cops_new = [
    3.63,
    3.99 
]

cool_cops_ex = [
    2.87,
    3.15,
    3.63,
    3.99 
]

heat_cops_new = [
    3.13,
    3.44 
]

heat_cops_ex = [
    2.61,
    2.87,
    3.13,
    3.44 
]

required_columns = [
    "case_name",
    ":cooling_coil_cop",
    ":heating_coil_cop"
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

    # Choose replacement lists
    filename = filepath.name

    if "&New&" in filename:
        case_names = case_names_new
        cool_cops = cool_cops_new
        heat_cops = heat_cops_new
    else:
        case_names = case_names_ex
        cool_cops = cool_cops_ex
        heat_cops = heat_cops_ex

    # Make sure the replacement lists match each other
    if len(case_names) != len(cool_cops):
        raise ValueError(
            f"{filepath}: case_names has {len(case_names)} values "
            f"but cool_cops has {len(cool_cops)} values."
        )

    # Make sure CSV has enough rows
    if len(df) < len(case_names):
        raise ValueError(
            f"{filepath} has only {len(df)} rows, but "
            f"{len(case_names)} replacement values are required."
        )

    # Delete extra rows
    df = df.iloc[:len(case_names)].copy()

    # Replace columns
    df["case_name"] = case_names
    df[":cooling_coil_cop"] = cool_cops
    df[":heating_coil_cop"] = heat_cops

    # Save over original file
    df.to_csv(filepath, index=False)

    print(
        f"  Updated successfully: "
        f"{'New' if '&New&' in filename else 'Ex'} - "
        f"{len(case_names)} rows"
    )

print("All files complete.")