
"""
A Utility to redirect tqdm progress bar to a log file instead of stdout.
"""

__version__      = '1.0.0d'
__author__       = 'Adarsh Anand'
__author_email__ = 'adarsh.a1@karza.in'
__license__      = 'GNU General Public License v3.0'
__url__          = 'https://github.com/adarsh-anand15/tqdm_logger'


import io
import os

__all__ = ['TqdmLogger']

class TqdmLogger(io.StringIO):
    """
        Output stream for tqdm which will output to log file instead of
        the stdout. 
        
        It is necessary to reset the logger stream everytime before starting a new tqdm progress bar.
    """

    def __init__(self, log_file):
        """
        Initialize with a log file to use for logging, 
        a buf to catch logs, and a bar index that stores the line number of the bar in file, 
        initialized to -1 to indicate that progress bar has not started yet.
        
        Args:
            log_file (str): Path of the file to write logs into

        """

        super(TqdmLogger, self).__init__()
        self.logger = log_file
        self.buf = ''
        self.bar_index = -1

        # Create the log file if it doesn't already exists
        if not os.path.isfile(self.logger):
            fstream = open(self.logger, 'w')
            fstream.close()

        
    def reset(self):
        """
        Reset the bar index to -1 before starting a new progress bar
        to avoid updating an earlier progress bar.
        """

        self.bar_index = -1
        
    def write(self, buf):
        """
        Capture the buf to be written.
        """

        self.buf = buf.strip('\r\n\t ')
    
    def flush(self):
        """
        Update the progress bar. It does that by reading the entire file content, replacing the line
        containing the progress bar, and writes back everything.
        """

        #skip if buffer is empty
        if not self.buf.strip():
            return
          
        # Read the entire content of the log file
        ifstream = open(self.logger, 'r')
        lines = ifstream.readlines()
        ifstream.close()
        
        # Replace the progress bar line with new value
        if self.bar_index == -1:
            lines.append(self.buf.strip())
            self.bar_index = len(lines) - 1
        else:
            lines[self.bar_index] = self.buf.strip()
            
        for i, line in enumerate(lines):
            lines[i] = line.strip() + '\n'
        
        # write back everything
        ofstream = open(self.logger, 'w')
        ofstream.writelines(lines)
        ofstream.close()
        
        # reset the buffer for next cycle
        self.buf = ''