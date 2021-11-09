# TQDM Logger

>> A utility to log tqdm progress bars into a file instead of stdout.

## Description

Well we all use tqdm progress bars to track the progress of a running code. Sometimes we would like to log those progress bars in a log file instead of stdout. Using tqdm as is has a problem. It write each update in a newline. This utility is to solve this problem and be able to update progress bars inplace.

## General Usage

Use the TqdmLogger class to declare a log stream handler with a log file, and pass that to tqdm's file argument. Thats it!!!

### Example Usage

~~~python
import time

from tqdm_logger import TqdmLogger

log_file = 'temp_log.log'

tqdm_stream = TqdmLogger(log_file)

tqdm_stream.reset()

for x in tqdm(range(100), file = tqdm_stream):

    time.sleep(.5)
