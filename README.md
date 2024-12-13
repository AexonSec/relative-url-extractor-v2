# Endpoint Extractor Tool

A Python tool to extract endpoints (e.g., API paths) from JavaScript files using regex.

## Features

- **Sanitization of Non-ASCII Characters**: Ensures compatibility with various file encodings.
- **Regex Matching**: Extracts endpoints enclosed in single or double quotes.
- **Command-Line Options**:
  - Specify the JavaScript file to analyze.
  - Optionally display the full line containing the endpoint.

## Requirements

- Python 3.6 or later

## Installation

1. Clone the repository or download the script file.
2. Ensure the script is executable:
   ```bash
   chmod +x extract_endpoints.py
   ```

## Usage

### Basic Usage

To extract endpoints from a JavaScript file:
```bash
./extract_endpoints.py path/to/file.js
```

### Show Full Lines

To display the full line containing the endpoint, use the `--show-line` flag:
```bash
./extract_endpoints.py path/to/file.js --show-line
```
<img src="https://github.com/AexonSec/relative-url-extractor-v2/blob/main/demo.PNG" />

### Example

Suppose you have a file `example.js` containing:
```javascript
const apiEndpoint = "/api/v1/users";
const anotherEndpoint = '/api/v2/orders';
```
Running the script:
```bash
./extract_endpoints.py example.js
```
Output:
```
/api/v1/users
/api/v2/orders
```

With the `--show-line` flag:
```bash
./extract_endpoints.py example.js --show-line
```
Output:
```
/api/v1/users
------------------------------------------------
const apiEndpoint = "/api/v1/users";

/api/v2/orders
------------------------------------------------
const anotherEndpoint = '/api/v2/orders';
```

## Error Handling

- If the specified file does not exist, an error message will be displayed.
- If any unexpected error occurs, the script will output the error message and exit.

## License

This tool is released under the MIT License.

