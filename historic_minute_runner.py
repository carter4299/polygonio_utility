import sched
import time
import psutil
from historic_minute import PolygonMin


"""
for custom timestamp per ticker use ----->

def main(ticker, unix_tstamp):
    #all_data = PolygonMin('your_api_key', r'C:\\Users\you\Desktop\your_folder',
     #'ticker[index]', unix timestamp[index])
    global index += 1
    all_data = PolygonMin(api_key, out_folder, ticker, unix_tstamp)
    all_data.generate_timestamps()
    all_data.main()


tickers = []
timestamps = []
"""


def running(ticker):
    """ all_data = PolygonMin('your_api_key', r'C:\\Users\you\Desktop\your_folder',
     'ticker[index]',unix timestamp)    |    set variables on line 59-63"""
    global index
    index += 1
    all_data = PolygonMin(api_key, out_folder, ticker, unix_tstamp)
    all_data.generate_timestamps()
    all_data.main()


def run_script(sc):
    print(f"Running .... {tickers[index]}")
    start_time = time.perf_counter()
    cpu_percent_start = psutil.cpu_percent()
    cpu_percent_max = cpu_percent_start

    running(tickers[index])

    end_time = time.perf_counter()
    runtime = end_time - start_time

    cpu_percent_end = psutil.cpu_percent()
    cpu_percent_avg = (cpu_percent_start + cpu_percent_end) / 2

    if cpu_percent_end > cpu_percent_max:
        cpu_percent_max = cpu_percent_end

    print(f"Runtime: {runtime:.2f} seconds\nAverage CPU usage: {cpu_percent_avg:.2f}%"
      f"\nMax CPU usage: {cpu_percent_max:.2f}%")

    s.enter(60 + runtime, 1, run_script, (sc,))


s = sched.scheduler(time.time, time.sleep)
index = 0
api_key = ''
out_folder = r''
tickers = []
unix_tstamp = 0000000000000
s.enter(60, 1, run_script, (s,))
s.run()
