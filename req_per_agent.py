from collections import defaultdict
from helper import LogParser

class UserAgentRequestCounter:
    """
    Parses a log file and counts the number of requests made by each user agent.
    """

    def __init__(self, log_file_path):
        """
        Initializes the log parser and sets the log file path.

        Args:
            log_file_path (str): Path to the log file to be analyzed.
        """
        self.log_file_path = log_file_path
        self.parser = LogParser()  # Custom log parser to extract log data
        self.user_agent_counts = defaultdict(int)  # Dictionary to track request counts per user agent

    def count_requests(self):
        """
        Reads the log file line by line, extracts user agent data,
        and counts how many times each user agent appears.
        """
        try:
            with open(self.log_file_path, 'r') as log_file:
                for line in log_file:
                    data = self.parser.parse_log_line(line)
                    if data and 'user_agent' in data:
                        user_agent = data['user_agent']
                        self.user_agent_counts[user_agent] += 1
        except FileNotFoundError:
            print(f"Error: Log file '{self.log_file_path}' not found.")

    def display_results(self):
        """
        Displays the number of requests made by each user agent.
        """
        for user_agent, count in self.user_agent_counts.items():
            print(f"{user_agent}: {count} requests")

# Example usage
if __name__ == "__main__":
    log_path = './NodeJsApp.log'
    counter = UserAgentRequestCounter(log_path)
    counter.count_requests()
    counter.display_results()
