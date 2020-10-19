import unittest
from datetime import datetime, timezone
import purpleair

class TestWrite(unittest.TestCase):

    def test_get_filedir_and_name(self):
        run_time_fixture = datetime(2020, 9, 8, 15)
        self.assertEqual(purpleair.write.get_filedir_and_name(run_time_fixture, 'output'), ('output/2020/09/08', '15.csv'), 'Should be formatted with zero padding and 24 hour time')

    def test_write_to_csv(self):
        records_fixture = [
            {'sensorid': 14633,'latitude': 37.275561,'longitude': -121.964134,'pm25': '7.83','time': 1603060519},
            {'sensorid': 14634,'latitude': 37.275561,'longitude': -121.964134,'pm25': '8.74','time': 1603060519},
            {'sensorid': 25999,'latitude': 30.053808,'longitude': -95.494643,'pm25': '12.68','time': 1603060470}
        ]
        fieldnames_fixture = ['sensorid',
                            'latitude',
                            'longitude',
                            'time',
                            'pm25']
        run_time_fixture = datetime(2020, 9, 8, 15)
        purpleair.write.write_to_csv(records_fixture, fieldnames_fixture, run_time_fixture, 'test-output')

if __name__ == '__main__':
    unittest.main()
