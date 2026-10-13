# Build script (after simulation)
# Runs locally, assume all files are where you expect them to be.
# Assume that DEER-UES-Tool scripts are available in the environment (resul3.py).
function collect(**kwargs) {

    # All the steps that need to read directly from model output files.
    # Also, this function should write a file collect.json containing a list of output filenames.

    outputs = []
    # (Solaris version) Collect simulation values: usage, hourly data, metadata
    deer_ues_tool_path = kwargs.get('deer_ues_tool_path', '')
    python $deer_ues_tool_path/result3.py --normunitquery SWHC027_normunit_query.txt
    outputs += 'simdata.sqlite'
    # Future syntax:
    python -m deer-ues-tool.collect --normunitquery SWHC027_normunit_query.txt
    # (DNV version)
    # You may need to save a copy of MFm.py in the measure folder and fill in the blanks - measure folder, version, etc.
    python ./MFm.py ...
    outputs += 'DEER_loadshapes.zip'

    # Write the list of collected output files to collect.json
    with open('collect.json', 'w') as f:
        import json
        json.dump(outputs, f)
}

function calculate(**kwargs) {
    # Steps that can reference other output files (not directly from model output)
    # Also, this function should write a file calculate.json containing a list of output filenames.

    outputs = []
    # Solaris post-processing steps
    python $deer_ues_tool_path/post_processing.py --coilfilter SWHC027_coil_filter.csv
    outputs += 'simdata.sqlite'
    # Future syntax:
    python -m deer-ues-tool.calculate --coilfilter SWHC027_coil_filter.csv

    # DNV post-processing scripts with PostgreSQL
    ...

    # Write the list of calculated output files to calculate.json
    with open('calculate.json', 'w') as f:
        import json
        json.dump(outputs, f)

}

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Run collection and calculation steps")
    parser.add_argument('--collect', action='store_true', help="Run the collect steps")
    parser.add_argument('--calculate', action='store_true', help="Run the calculate steps")
    parser.add_argument('--deer_ues_tool_path', type=str, default='', help="Path to the DEER-UES-Tool scripts")
    args = parser.parse_args()

    if args.collect:
        collect(deer_ues_tool_path=args.deer_ues_tool_path)
    if args.calculate:
        calculate(deer_ues_tool_path=args.deer_ues_tool_path)
        
if __name__ == "__main__":
    main()
