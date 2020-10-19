class Config:
    def __init__(self):
        self.url = 'https://www.purpleair.com/json'
        self.column_to_property = {
            'sensorid': 'ID',
            'latitude': 'Lat',
            'longitude': 'Lon',
            'time': 'LastSeen',
            'pm25': 'PM2_5Value'
        }
        self.fieldnames = ['sensorid', 'latitude', 'longitude', 'time', 'pm25']
        self.output_dir = 'output'

