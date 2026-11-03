import pandas as pd
from pathlib import Path

# CSV files
csv_files = [
    # Com Ex
    Path(r"C:\Projects\dev-SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_Ex\cases\MBT&0&cPTAC&Ex&dxAC_equip__pkgTerm.csv"),
    Path(r"C:\Projects\dev-SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_Ex\cases\MLI&0&cPTAC&Ex&dxAC_equip__pkgTerm.csv"),
    Path(r"C:\Projects\dev-SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_Ex\cases\Mtl&0&cPTAC&Ex&dxAC_equip__pkgTerm.csv"),
    Path(r"C:\Projects\dev-SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_Ex\cases\Nrs&0&cPTAC&Ex&dxAC_equip__pkgTerm.csv"),
    Path(r"C:\Projects\dev-SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_Ex\cases\OfL&0&cPTAC&Ex&dxAC_equip__pkgTerm.csv"),
    Path(r"C:\Projects\dev-SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_Ex\cases\OfS&0&cPTAC&Ex&dxAC_equip__pkgTerm.csv"),
    Path(r"C:\Projects\dev-SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_Ex\cases\RFF&0&cPTAC&Ex&dxAC_equip__pkgTerm.csv"), 
    Path(r"C:\Projects\dev-SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_Ex\cases\RtS&0&cPTAC&Ex&dxAC_equip__pkgTerm.csv"),
    Path(r"C:\Projects\dev-SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_Ex\cases\WRf&0&cPTAC&Ex&dxAC_equip__pkgTerm.csv"),
    # Htl Ex
    Path(r"C:\Projects\dev-SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_Htl_Ex\cases\Htl&0&cPTAC&Ex&dxAC_equip__pkgTerm.csv"),
    # Htl New
    Path(r"C:\Projects\dev-SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_Htl_New\cases\Htl&0&cPTAC&New&dxAC_equip__pkgTerm.csv"),
    # Com New
    Path(r"C:\Projects\dev-SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_New\cases\MBT&0&cPTAC&New&dxAC_equip__pkgTerm.csv"),
    Path(r"C:\Projects\dev-SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_New\cases\MLI&0&cPTAC&New&dxAC_equip__pkgTerm.csv"),
    Path(r"C:\Projects\dev-SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_New\cases\Mtl&0&cPTAC&New&dxAC_equip__pkgTerm.csv"),
    Path(r"C:\Projects\dev-SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_New\cases\Nrs&0&cPTAC&New&dxAC_equip__pkgTerm.csv"),
    Path(r"C:\Projects\dev-SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_New\cases\OfL&0&cPTAC&New&dxAC_equip__pkgTerm.csv"),
    Path(r"C:\Projects\dev-SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_New\cases\OfS&0&cPTAC&New&dxAC_equip__pkgTerm.csv"),
    Path(r"C:\Projects\dev-SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_New\cases\RFF&0&cPTAC&New&dxAC_equip__pkgTerm.csv"), 
    Path(r"C:\Projects\dev-SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_New\cases\RtS&0&cPTAC&New&dxAC_equip__pkgTerm.csv"),
    Path(r"C:\Projects\dev-SWHC027-09\commercial measures\SWHC027-09 Package Terminal ACHP\SWHC027-09 Package Terminal ACHP_New\cases\WRf&0&cPTAC&New&dxAC_equip__pkgTerm.csv"),
]


case_names_new = [
    "NE-dxAC_equip-pkgTerm-EER-10.70-Std",
    "NE-dxAC_equip-pkgTerm-EER-11.77-Msr"
]

case_names_ex = [
    "NE-dxAC_equip-pkgTerm-EER-8.56-Std",
    "NE-dxAC_equip-pkgTerm-EER-9.42-Msr",
    "NE-dxAC_equip-pkgTerm-EER-10.70-Std",
    "NE-dxAC_equip-pkgTerm-EER-11.77-Msr"
]

cool_cops_new = [
    3.63,
    3.99 
]

cool_cops_ex = [
    2.90,
    3.19,
    3.63,
    3.99 
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

    # Choose replacement lists based on Ex vs New
    filename = filepath.name

    if "&Ex&" in filename:
        case_names = case_names_ex
        cool_cops = cool_cops_ex

    elif "&New&" in filename:
        case_names = case_names_new
        cool_cops = cool_cops_new

    else:
        raise ValueError(
            f"{filepath}: could not determine whether this is Ex or New."
        )

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
    df[":main_cool_coil_cop"] = cool_cops

    # Save over original file
    df.to_csv(filepath, index=False)

    print(
        f"  Updated successfully: "
        f"{'Ex' if '&Ex&' in filename else 'New'} - "
        f"{len(case_names)} rows"
    )

print("All files complete.")