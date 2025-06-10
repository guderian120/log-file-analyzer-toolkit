from collections import defaultdict
from datetime import timedelta
from helper import LogParser

class RequestAnalyzer:
    def __init__(self, log_file_path):
        self.log_file_path = log_file_path
        self.ip_requests = defaultdict(list)
        self.log_parser = LogParser()

    def parse_log_file(self):
        """Reads and parses the log file, storing IP requests."""
        with open(self.log_file_path) as f:
            for line in f:
                data = self.log_parser.parse_log_line(line)
                if data:
                    self.ip_requests[data['ip']].append(data['timestamp'])

    def count_requests_in_window(self, window_seconds=10):
        """
        Counts requests within a time window after the first request per IP.
        
        Args:
            window_seconds (int): Time window in seconds to count requests after first request.
        
        Returns:
            dict: A dictionary mapping IPs to their request counts in the specified window.
        """
        results = {}
        for ip, timestamps in self.ip_requests.items():
            timestamps.sort()
            first = timestamps[0]
            count = sum(1 for t in timestamps 
                        if timedelta(seconds=0) < (t - first) <= timedelta(seconds=window_seconds))
            results[ip] = count
        return results

    def print_results(self, window_seconds=10):
        """Prints the request counts for each IP in the specified time window."""
        results = self.count_requests_in_window(window_seconds)
        for ip, count in results.items():
            print(f"{ip}: {count} requests in {window_seconds}s after first")

if __name__ == "__main__":
    import os
    import sys
    
    def get_valid_path():
        while True:
            path = input("Enter log file path: ").strip()
            if os.path.isfile(path):
                return path
            print(f"File not found: {path}")
    
    try:
        log_path = './NodeJsApp.log'
        if not os.path.exists(log_path):
            print("Default log file not found")
            log_path = get_valid_path()
        
        analyzer = RequestAnalyzer(log_path)
        analyzer.parse_log_file()
        analyzer.print_results(window_seconds=10)
        
    except Exception as e:
        print(f"Analysis failed: {e}", file=sys.stderr)
        sys.exit(1)