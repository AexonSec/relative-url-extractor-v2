#!/usr/bin/env python3
import re
import sys
import argparse
import requests

EXCERPT_FORMAT = "------------------------------------------------\n%s\n"

# Function to sanitize non-ASCII characters
def sanitize_non_ascii(string):
    return string.encode('ascii', errors='replace').decode('ascii').replace('\ufffd', '_')

# Function to extract endpoints from content
def extract_endpoints(content, show_line=False):
    REGEX = re.compile(r'(["\'])(/[^"\']*[\w\d\W\?/&=#.!:_-]*?)\1')
    matched_endpoints = []

    print("\n[ Extracted Endpoints ]")
    print("-" * 60)
    for idx, match in enumerate(REGEX.finditer(content), start=1):
        full_match, endpoint = match.group(0), match.group(2)
        if endpoint not in matched_endpoints:
            matched_endpoints.append(endpoint)
            print(f"{idx:02d}. Endpoint: {endpoint}")
            if show_line:
                print(f"    Full Match: {full_match}")
                print("-" * 60)
    if not matched_endpoints:
        print("No endpoints found.")
    print("-" * 60)


# Function to get content from a file or URL
def get_content(source):
    try:
        # Check if source is a URL or a local file
        if source.startswith("http://") or source.startswith("https://"):
            response = requests.get(source)
            response.raise_for_status()  # Will raise an exception for HTTP error responses
            return response.text
        else:
            with open(source, "r", encoding="utf-8") as f:
                return f.read()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: File '{source}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

# Main function
def main():
    parser = argparse.ArgumentParser(description="Extract endpoints from JavaScript files or URLs.")
    parser.add_argument("source", help="Path to the JavaScript file or URL to be analyzed.")
    parser.add_argument("--show-line", action="store_true", help="Show the full line containing the endpoint.")
    args = parser.parse_args()

    content = get_content(args.source)
    sanitized_content = sanitize_non_ascii(content)
    extract_endpoints(sanitized_content, args.show_line)

if __name__ == "__main__":
    main()
