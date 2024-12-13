import re
import sys

EXCERPT_FORMAT = "------------------------------------------------\n%s\n"

# Function to sanitize non-ASCII characters
def sanitize_non_ascii(string):
    return string.encode('ascii', errors='replace').decode('ascii').replace('\ufffd', '_')

# Read input from STDIN
contents = "".join(sys.stdin.readlines())

# Regex to match the desired pattern
REGEX = re.compile(r"(^.*?(["'])(/[\w\d\W\?/&=#.!:_-]*?)\2.*$)")

# List to track matched endpoints
matched_endpoints = []

# Process the sanitized input
sanitized_contents = sanitize_non_ascii(contents).replace(';', '\n')

for match in REGEX.findall(sanitized_contents):
    full_match, quote, endpoint = match
    if endpoint not in matched_endpoints:
        matched_endpoints.append(endpoint)
        print(endpoint)
        if '--show-line' in sys.argv:
            print(EXCERPT_FORMAT % full_match)
