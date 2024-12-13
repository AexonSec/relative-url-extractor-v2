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
or
```bash
./extract_endpoints.py https://example.com/path/to/file.js
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
[ Extracted Endpoints ]
------------------------------------------------------------
01. Endpoint: /participants
    Full Match: "participants"
------------------------------------------------------------
02. Endpoint: /bugs
    Full Match: "/bugs"
------------------------------------------------------------
03. Endpoint: /invitations/
    Full Match: "/invitations/"
------------------------------------------------------------
04. Endpoint: /
    Full Match: "/"
------------------------------------------------------------
05. Endpoint: /directory?query=type%3Ahackerone
    Full Match: "/directory?query=type%3Ahackerone"
------------------------------------------------------------
06. Endpoint: /0h8
    Full Match: "/0h8"
------------------------------------------------------------
07. Endpoint: /4Ms
    Full Match: "/4Ms"
------------------------------------------------------------
08. Endpoint: /6Z6
    Full Match: "/6Z6"
------------------------------------------------------------
09. Endpoint: /6ei
    Full Match: "/6ei"
------------------------------------------------------------
10. Endpoint: /820
    Full Match: "/820"
------------------------------------------------------------
11. Endpoint: /programs/search?query=bounties%3Ayes&sort=name%3Aascending&limit=1000
    Full Match: "/programs/search?query=bounties%3Ayes&sort=name%3Aascending&limit=1000"
------------------------------------------------------------

```

## Error Handling

- If the specified file does not exist, an error message will be displayed.
- If any unexpected error occurs, the script will output the error message and exit.

## License

This tool is released under the MIT License.

