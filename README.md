# Log Analyzer

The **Log Analyzer** is a Python-based tool designed to analyze log files, providing various extraction and search functionalities. It allows users to extract emails, IP addresses, timestamps, and more from log files, as well as search for custom patterns using regular expressions.

## Features
- **Search by Keyword**: Search for specific keywords within the log file.
- **Extract Emails**: Extract all email addresses found in the log file.
- **Extract IPs**: Extract all IP addresses present in the log file.
- **Count IP Occurrences**: Count how many times each IP address appears in the log file.
- **Extract Timestamps with IPs**: Extract timestamps along with the associated IP addresses.
- **Extract Full Log Entries**: Extract complete log entries based on IP addresses, timestamps, or specific keywords.
- **Search by Custom Regex**: Perform custom regex searches on the log file.

## How It Works
1. **Log File Input**:
   - The program prompts the user to input the path or filename of the log file.
   - It checks if the file exists and reads its content for further analysis.

2. **Extraction Functions**:
   - **Emails**: The program uses regular expressions (regex) to identify and extract email addresses from the log file.
   - **IPs**: It identifies IP addresses using a predefined regex pattern.
   - **Timestamps**: The program extracts timestamped entries formatted as `YYYY-MM-DD HH:MM:SS`.
   
3. **Log Analysis**:
   - The program offers a menu-driven interface where users can select different actions such as searching for specific keywords, extracting data, or running custom regex queries.

4. **Custom Regex Search**:
   - Users can input their own regular expression pattern, and the program will search the log file for matches.

## Installation

### Dependencies
This project uses Python's built-in libraries, so there are no external dependencies to install. Ensure you are using Python 3.x or later.

## Usage

### Main Menu
After starting the program, the user will see a menu with the following options:
1. **Search by keyword**: Search for a specific keyword in the log file.
2. **Extract all emails**: Extract all email addresses from the log file.
3. **Extract all IPs**: Extract all IP addresses from the log file.
4. **Count IP occurrences**: Count how many times each IP address appears in the log file.
5. **Extract timestamps with IPs**: Extract timestamps and associated IP addresses.
6. **Extract full log entries by IP, timestamp, or keyword**: Extract entire log entries containing a specific IP, timestamp, or keyword.
7. **Search by custom regex**: Perform a custom regex search.
8. **Exit**: Exit the program.

### Example Output

#### Search by Keyword
```plaintext
--- Log Analyzer Menu ---
1. Search by keyword
...
Select an option (1-8): 1
Enter the keyword to search: error
error occurred at 2023-07-10 12:34:56 from 192.168.1.1
```

#### Extract Emails
```plaintext
--- Log Analyzer Menu ---
2. Extract all emails
...
Select an option (1-8): 2
example@example.com
user@domain.com
```

#### Count IP Occurrences
```plaintext
--- Log Analyzer Menu ---
4. Count IP occurrences
...
Select an option (1-8): 4
192.168.1.1: 3 times
10.0.0.2: 1 time
```

#### Custom Regex Search
```plaintext
--- Log Analyzer Menu ---
7. Search by custom regex
...
Select an option (1-8): 7
Enter the custom regex pattern: \d{3}-\d{3}-\d{4}
Match found: 123-456-7890
```

## Contributing
Feel free to fork the repository, improve the code, and submit a pull request.

## License
This project is open-source and available for modification and distribution.