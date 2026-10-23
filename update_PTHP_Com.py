import pandas as pd
from pathlib import Path

# CSV files
csv_files = [
    # Com Ex
    Path(r"C:\Projects\SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_Ex\cases\MBT&0&cPTHP&Ex&dxHP_equip__pkgTerm.csv"),
    Path(r"C:\Projects\SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_Ex\cases\MLI&0&cPTHP&Ex&dxHP_equip__pkgTerm.csv"),
    Path(r"C:\Projects\SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_Ex\cases\Mtl&0&cPTHP&Ex&dxHP_equip__pkgTerm.csv"),
    Path(r"C:\Projects\SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_Ex\cases\Nrs&0&cPTHP&Ex&dxHP_equip__pkgTerm.csv"),
    Path(r"C:\Projects\SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_Ex\cases\OfL&0&cPTHP&Ex&dxHP_equip__pkgTerm.csv"),
    Path(r"C:\Projects\SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_Ex\cases\OfS&0&cPTHP&Ex&dxHP_equip__pkgTerm.csv"),
    Path(r"C:\Projects\SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_Ex\cases\RFF&0&cPTHP&Ex&dxHP_equip__pkgTerm.csv"), 
    Path(r"C:\Projects\SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_Ex\cases\RtS&0&cPTHP&Ex&dxHP_equip__pkgTerm.csv"),
    Path(r"C:\Projects\SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_Ex\cases\WRf&0&cPTHP&Ex&dxHP_equip__pkgTerm.csv"),
    # Htl Ex
    Path(r"C:\Projects\SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_Htl_Ex\cases\Htl&0&cPTHP&Ex&dxHP_equip__pkgTerm.csv"),
    # Htl New
    Path(r"C:\Projects\SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_Htl_New\cases\Htl&0&cPTHP&New&dxHP_equip__pkgTerm.csv"),
    # Com New
    Path(r"C:\Projects\SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_New\cases\MBT&0&cPTHP&New&dxHP_equip__pkgTerm.csv"),
    Path(r"C:\Projects\SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_New\cases\MLI&0&cPTHP&New&dxHP_equip__pkgTerm.csv"),
    Path(r"C:\Projects\SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_New\cases\Mtl&0&cPTHP&New&dxHP_equip__pkgTerm.csv"),
    Path(r"C:\Projects\SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_New\cases\Nrs&0&cPTHP&New&dxHP_equip__pkgTerm.csv"),
    Path(r"C:\Projects\SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_New\cases\OfL&0&cPTHP&New&dxHP_equip__pkgTerm.csv"),
    Path(r"C:\Projects\SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_New\cases\OfS&0&cPTHP&New&dxHP_equip__pkgTerm.csv"),
    Path(r"C:\Projects\SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_New\cases\RFF&0&cPTHP&New&dxHP_equip__pkgTerm.csv"), 
    Path(r"C:\Projects\SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_New\cases\RtS&0&cPTHP&New&dxHP_equip__pkgTerm.csv"),
    Path(r"C:\Projects\SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_New\cases\WRf&0&cPTHP&New&dxHP_equip__pkgTerm.csv"),
]


# Same values will be pasted into EVERY CSV
case_names = [
    "NE-dxHP_equip-pkgTerm-EER-9.31-Std",
    "NE-dxHP_equip-pkgTerm-EER-8.46-Std",
    "NE-dxHP_equip-pkgTerm-EER-7.61-Std",
    "NE-dxHP_equip-pkgTerm-EER-11.9-Std",
    "NE-dxHP_equip-pkgTerm-EER-10.70-Std",
    "NE-dxHP_equip-pkgTerm-EER-9.5-Std",
    "NE-dxHP_equip-pkgTerm-EER-10.24-Msr",
    "NE-dxHP_equip-pkgTerm-EER-9.31-Msr",
    "NE-dxHP_equip-pkgTerm-EER-8.37-Msr",
    "NE-dxHP_equip-pkgTerm-EER-13.09-Msr",
    "NE-dxHP_equip-pkgTerm-EER-11.77-Msr",
    "NE-dxHP_equip-pkgTerm-EER-10.45-Msr"
]

cool_cops = [
    3.15,
    2.87,
    2.58,
    4.03,
    3.63,
    3.22,
    3.47,
    3.15,
    2.84,
    4.43,
    3.99,
    3.54
]

heat_cops = [
    2.72,
    2.61,
    2.51,
    3.34,
    3.13,
    2.92,
    2.99,
    2.87,
    2.76,
    3.67,
    3.44,
    3.21
]


required_columns = [
    "case_name",
    ":main_cool_coil_cop",
    ":main_heat_coil_cop"
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
        == len(heat_cops)
    ):
        raise ValueError(
            f"{filepath} has {len(df)} rows, but the replacement "
            f"lists have {len(case_names)} values."
        )

    # Replace the three columns in order
    df["case_name"] = case_names
    df[":main_cool_coil_cop"] = cool_cops
    df[":main_heat_coil_cop"] = heat_cops

    # Save over original file
    df.to_csv(filepath, index=False)

    print("  Updated successfully")

print("All files complete.")