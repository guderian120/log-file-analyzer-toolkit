
# Log File Analyzer

A Python toolkit for analyzing web server log files with three specialized modules.

## 📦 Modules

1. **Endpoint Hit Counter**  
   - Counts URL endpoint access frequency
   - `endpoint_hits.py`

2. **User Agent Analyzer**  
   - Tracks client device/browser distribution  
   - `req_per_agent.py`

3. **Request Pattern Detector**  
   - Identifies potential DDoS patterns by IP request frequency  
   - `request_in_10_secs.py`

## 🛠️ Setup

```bash
git clone https://github.com/guderian120/log-file-analyzer.git
cd log-file-analyzer
```

## 🚀 Usage

```python
# Endpoint analysis
python endpoint_hits.py NodeJsApp.log

# User agent analysis 
python req_per_agent.py NodeJsApp.log

# Request burst detection
python request_in_10_secs.py NodeJsApp.log
```

## 📊 Sample Output

```
/api/users: 142 hits
Chrome/91.0: 85 requests 
192.168.1.1: 24 requests in 10s window
```

## 📝 Requirements
- Python 3.8+
- Standard library only (no external dependencies)

## 🏗️ Structure
```
log-file-analyzer/
├── endpoint_hits.py
├── req_per_agent.py
├── request_in_10_secs.py
├── helper.py
└── NodeJsApp.log (sample)
```

---
