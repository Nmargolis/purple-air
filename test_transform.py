import unittest
import purpleair
from config import Config

config = Config()

class TestTransform(unittest.TestCase):

    def test_transform(self):
        results_input = [
            {'ID': 14633, 'Label': ' Hazelwood canary ', 'DEVICE_LOCATIONTYPE': 'outside', 'THINGSPEAK_PRIMARY_ID': '559921', 'THINGSPEAK_PRIMARY_ID_READ_KEY': 'CU4BQZZ38WO5UJ4C', 'THINGSPEAK_SECONDARY_ID': '559922', 'THINGSPEAK_SECONDARY_ID_READ_KEY': 'D0YNZ1LM59LL49VQ', 'Lat': 37.275561, 'Lon': -121.964134, 'PM2_5Value': '7.83', 'LastSeen': 1603060519, 'Type': 'PMS5003+PMS5003+BME280', 'Hidden': 'false', 'isOwner': 0, 'humidity': '13', 'temp_f': '100', 'pressure': '1006.79', 'AGE': 0, 'Stats': '{"v": 7.83,"v1": 8.0,"v2": 9.04,"v3": 9.66,"v4": 8.02,"v5": 7.2,"v6": 18.77,"pm": 7.83,"lastModified": 1603060519935,"timeSinceModified": 120002}'},
            {'ID': 14634, 'ParentID': 14633, 'Label': ' Hazelwood canary  B', 'THINGSPEAK_PRIMARY_ID': '559923', 'THINGSPEAK_PRIMARY_ID_READ_KEY': 'DULWDNCI9M6PCIPC', 'THINGSPEAK_SECONDARY_ID': '559924', 'THINGSPEAK_SECONDARY_ID_READ_KEY': 'EY2CNMYRUZHDW1AL', 'Lat': 37.275561, 'Lon': -121.964134, 'PM2_5Value': '8.74', 'LastSeen': 1603060519, 'Hidden': 'false', 'isOwner': 0, 'AGE': 0, 'Stats': '{"v": 8.74,"v1": 8.26,"v2": 9.21,"v3": 9.81,"v4": 8.12,"v5": 7.2,"v6": 18.34,"pm": 8.74,"lastModified": 1603060519936,"timeSinceModified": 120002}'},
            {'ID': 25999, 'Label': ' Villages of Bridgestone AQI', 'DEVICE_LOCATIONTYPE': 'outside', 'THINGSPEAK_PRIMARY_ID': '694803', 'THINGSPEAK_PRIMARY_ID_READ_KEY': 'OO5PFS7JTQQSHQHE', 'THINGSPEAK_SECONDARY_ID': '694804', 'THINGSPEAK_SECONDARY_ID_READ_KEY': 'LW93B1YLLZ4N4QFM', 'Lat': 30.053808, 'Lon': -95.494643, 'PM2_5Value': '12.68', 'LastSeen': 1603060470, 'Type': 'PMS5003+PMS5003+BME280', 'Hidden': 'false', 'isOwner': 0, 'humidity': '44', 'temp_f': '93', 'pressure': '1010.13', 'AGE': 1, 'Stats': '{"v": 12.68,"v1": 13.18,"v2": 13.33,"v3": 13.64,"v4": 16.73,"v5": 15.63,"v6": 17.03,"pm": 12.68,"lastModified": 1603060470446,"timeSinceModified": 120009}'}
        ]
        expected_transformed = [
            {'sensorid': 14633,'latitude': 37.275561,'longitude': -121.964134,'pm25': '7.83','time': 1603060519},
            {'sensorid': 14634,'latitude': 37.275561,'longitude': -121.964134,'pm25': '8.74','time': 1603060519},
            {'sensorid': 25999,'latitude': 30.053808,'longitude': -95.494643,'pm25': '12.68','time': 1603060470}
        ]
        self.assertEqual(purpleair.transform.transform_results(results_input,config.column_to_property), expected_transformed, 'Data is transformed correctly')

if __name__ == '__main__':
    unittest.main()
