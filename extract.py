#!/usr/bin/env python3
import re
import sys
import argparse

EXCERPT_FORMAT = "------------------------------------------------\n%s\n"

# Function to sanitize non-ASCII characters
def sanitize_non_ascii(string):
    return string.encode('ascii', errors='replace').decode('ascii').replace('\ufffd', '_')

# Function to extract endpoints from content
def extract_endpoints(content, show_line=False):
    REGEX = re.compile(r'(["\'])(/[^"\']*[\w\d\W\?/&=#.!:_-]*?)\1')
    matched_endpoints = []

    for match in REGEX.finditer(content):
        full_match, endpoint = match.group(0), match.group(2)
        if endpoint not in matched_endpoints:
            matched_endpoints.append(endpoint)
            print(endpoint)
            if show_line:
                print(EXCERPT_FORMAT % full_match)

# Main function
def main():
    parser = argparse.ArgumentParser(description="Extract endpoints from JavaScript files.")
    parser.add_argument("file", help="Path to the JavaScript file to be analyzed.")
    parser.add_argument("--show-line", action="store_true", help="Show the full line containing the endpoint.")
    args = parser.parse_args()

    try:
        with open(args.file, "r", encoding="utf-8") as f:
            content = f.read()
            sanitized_content = sanitize_non_ascii(content)
            extract_endpoints(sanitized_content, args.show_line)
    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
