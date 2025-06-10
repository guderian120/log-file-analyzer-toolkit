
# 📊 Log File Analyzer

Python toolkit for analyzing web server logs with robust error handling and user-friendly prompts.

## 🛠️ Enhanced Features
- **Smart Error Recovery**: Auto-prompts for correct path when files are missing
- **User-Friendly**: Clear instructions and validation for file inputs
- **Graceful Exits**: Clean error messages and proper exit codes

## 📦 Modules

| Script | Description | Error Handling |
|--------|-------------|----------------|
| `endpoint_hits.py` | Counts URL endpoint frequency | ✔️ Auto-retry with new path |
| `req_per_agent.py` | Analyzes user agent distribution | ✔️ Keyboard interrupt support |
| `request_in_10_secs.py` | Detects request bursts by IP | ✔️ Interactive path input |

## Clone the repo
```bash
git clone   https://github.com/guderian120/log-file-analyzer-toolkit.git
cd log-file-analyzer-toolkit
```

## 🚀 Usage
```bash
python endpoint_hits.py
python req_per_agent.py  
python request_in_10_secs.py
```

**Sample Error Recovery Flow**:
```bash
$ python endpoint_hits.py
Error: Log file not found at ./NodeJsApp.log
Please enter correct log file path (or 'q' to quit): ../logs/myapp.log
/api/users: 215 hits
...
```

## 🛡️ Error Cases Handled
- Missing log files
- Invalid file paths  
- Keyboard interrupts (Ctrl+C)
- Permission errors
- Empty/malformed log files

## 📝 Requirements
```text
Python 3.8+
No external dependencies
```

## 🏗️ Project Structure
```bash
.
├── endpoint_hits.py      # With interactive path recovery
├── req_per_agent.py      # User agent analyzer
├── request_in_10_secs.py # Burst detection
├── helper.py            # Shared log parser
└── NodeJsApp.log        # Sample log
```

