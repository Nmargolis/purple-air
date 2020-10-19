from typing import List, Tuple
from datetime import datetime
import csv
import os
from pathlib import Path


def get_filedir_and_name(run_time: datetime, output_dir: str) -> Tuple[str, str]:
    """
    Takes a datetime and output dir, and generates a
    filedir and filename for the output file
    """
    return (f'{output_dir}/{run_time:%Y/%m/%d}', f'{run_time:%H}.csv')


def write_to_csv(results: List, fieldnames: List, run_time: datetime, output_dir: str) -> str:
    """
    Takes the results list of json data and writes them to a csv
    named YEAR/MONTH/DAY/HOUR.csv
    """
    filedir, filename = get_filedir_and_name(run_time, output_dir)
    filedir_path = Path(filedir)
    print('filedir_path', filedir_path)
    # Ensure the dirs exist
    filedir_path.mkdir(parents=True, exist_ok=True)
    filepath = filedir_path.joinpath(filename)
    print(f'Writing {len(results)} records to file: {filepath}')

    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)

