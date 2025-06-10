import re
from datetime import datetime

class LogParser:
    def __init__(self):
        self.log_pattern = re.compile(
            r'(?P<timestamp>\S+)\s+'
            r'(?P<ip>(?:\d{1,3}\.){3}\d{1,3}|[a-fA-F0-9:]+)\s+- -\s+'
            r'\[(?P<apache_time>.*?)\]\s+'
            r'"(?P<method>GET|POST|PUT|DELETE|HEAD)\s+'
            r'(?P<url>\S+)\s+'
            r'(?P<protocol>HTTP/\d\.\d)"\s+'
            r'(?P<status>\d+)\s+.*?\s+'
            r'"(?P<referrer>[^"]*)"\s+'
            r'"(?P<user_agent>[^"]*)"'
        )

    def parse_log_line(self, line):
        match = self.log_pattern.match(line)
        if match:
            data = match.groupdict()
            try:
                data['timestamp'] = datetime.strptime(data['timestamp'], "%Y-%m-%dT%H:%M:%S.%fZ")
            except ValueError:
                return None
            return data
        return None
