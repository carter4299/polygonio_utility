import pandas as pd
import requests
import os
import numpy as np
import time


class PolygonMin:
    def __init__(self, w, x, y, z):
        self.api_key = w
        self.o_folder = x
        self.ticker = y
        self.start_timestamp = z
        self.timestamps = []

    def generate_timestamps(self):
        """ generate all time stamps from start date to 1530491400000"""
        current_timestamp = self.start_timestamp
        while current_timestamp >= 1530491400000:
            self.timestamps.append(current_timestamp)
            current_timestamp -= (50000 * 60 * 1000)
        self.timestamps.append(1530491400000)
        np.array(self.timestamps)

    def main(self):
        """ iterate through timestamps(50,000 min each)"""
        for i, times in enumerate(self.timestamps[:-1]):
            end_date = times
            start = self.timestamps[i + 1]

            url = "https://api.polygon.io/v2/aggs/ticker/" + self.ticker + "/range/1/minute/" + str(start) + "/" + str(
                end_date) + "?adjusted=true&sort=asc&limit=50000&apiKey=" + self.api_key
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                df = pd.DataFrame(data['results'])
                o_file_path = os.path.join(self.o_folder, f'{self.ticker}_minute_pricing_{str(end_date)}.csv')
                df.to_csv(o_file_path, header='column_names', index=False)
                i += 1
                print(f'Completed: {(i / (len(self.timestamps) - 1)) * 100}%')
                time.sleep(20)
            else:
                print(f"Error fetching data from Polygon.io. Status code: {response.status_code}")
                time.sleep(30)


if __name__ == '__main__':
    """ all_data = PolygonMin('your_api_key', r'C:\\Users\you\Desktop\your_folder', 'ticker', unix timestamp) """
    all_data = PolygonMin('', r'', '', 0)
    all_data.generate_timestamps()
    all_data.main()
