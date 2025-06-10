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

# Example usage
if __name__ == "__main__":
    log_path = './NodeJsApp.log'
    counter = EndpointHitCounter(log_path)
    counter.count_hits()
    counter.display_results()
