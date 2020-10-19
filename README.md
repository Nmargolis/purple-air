# Purple Air hourly download pipeline
This project downloads the latest Purple Air data every hour, and stores the results in csvs like `output/YYYY/MM/DD/HH.csv`.
Each csv has columns: `sensorid,latitude,longitude,time,pm25`.
The `time` column is the UTC timestamp for when the sensor reading was last updated

## Setup
Install Prefect
- [See docs](https://docs.prefect.io/core/getting_started/installation.html)

Install dependencies
```
pip install -r requirements.txt
```

Create a Project
```
prefect create project 'Your Project Name'
```

Set up Prefect local orchestration for the first time
```
prefect backend server
```

## Run
Start a Prefect server
```
prefect server start
```

Register the main flow and start an agent
```
python main_flow.py 'Your Project Name'
```

## Test
So far, there are two unit test files:
- `test_transform.py`
- `test_write.py`
