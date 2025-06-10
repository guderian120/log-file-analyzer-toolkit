from collections import defaultdict
from helper import LogParser

class EndpointHitCounter:
    """
    A class to parse a log file and count the number of hits per endpoint.
    """

    def __init__(self, log_file_path):
        """
        Initialize the log parser and set the log file path.
        
        Args:
            log_file_path (str): Path to the log file.
        """
        self.log_file_path = log_file_path
        self.parser = LogParser()  # Instance of custom LogParser class
        self.endpoint_counts = defaultdict(int)  # Dictionary to hold hit counts per endpoint

    def count_hits(self):
        """
        Parses the log file and counts the number of hits per URL endpoint.
        """
        try:
            with open(self.log_file_path, 'r') as log_file:
                for line in log_file:
                    data = self.parser.parse_log_line(line)  # Parse each log line
                    if data and 'url' in data:
                        endpoint = data['url']
                        self.endpoint_counts[endpoint] += 1
        except FileNotFoundError:
            print(f"Error: Log file '{self.log_file_path}' not found.")

    def display_results(self):
        """
        Prints the number of hits for each endpoint.
        """
        for endpoint, count in self.endpoint_counts.items():
            print(f"{endpoint}: {count} hits")


if __name__ == "__main__":
    import os
    import sys
    
    default_log = './NodeJsApp.log'
    log_path = default_log
    
    while True:
        try:
            if not os.path.exists(log_path):
                print(f"Error: Log file not found at {log_path}")
                log_path = input("Please enter correct log file path (or 'q' to quit): ")
                if log_path.lower() == 'q':
                    sys.exit(0)
                continue
            
            counter = EndpointHitCounter(log_path)
            counter.count_hits()
            counter.display_results()
            break
            
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            retry = input("Try again with different file? (y/n): ")
            if retry.lower() != 'y':
                sys.exit(1)
            log_path = input("Enter new log file path: ")
