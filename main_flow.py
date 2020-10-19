import sys
from prefect import Flow, task, Client
from prefect.schedules import CronSchedule
from datetime import datetime, timedelta, timezone
from purpleair import fetch, transform, write
from config import Config

@task(name='Run time')
def get_run_time():
    run_time = datetime.now(timezone.utc)
    print(f'Running flow at {run_time:%Y-%m-%d %H:%M}')
    return run_time

@task(name='Fetch', max_retries=3, retry_delay=timedelta(seconds=30))
def fetch_results(config):
    return fetch.get_all_sensor_data(config.url)

@task(name='Transform')
def transform_results(config, results):
    return transform.transform_results(results, config.column_to_property)

@task(name='Write')
def write_results(config, results, run_time):
    return write.write_to_csv(results, config.fieldnames, run_time, config.output_dir)


def main(project_name):
    schedule = CronSchedule('0 * * * *')
    config = Config()
    with Flow('Purple Air hourly download flow', schedule) as flow:
        run_time = get_run_time
        fetch_result = fetch_results(config)
        transform_result = transform_results(config, fetch_result)
        write_results(config, transform_result, run_time)
    print(flow.register(project_name=project_name))
    flow.run_agent()

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print('A project name is required. Create one by running prefect create project \'Your Project Name\'. Then run python main_flow.py \'Your Project Name\'')
    else:
        project_name = sys.argv[1]
        main(project_name)
