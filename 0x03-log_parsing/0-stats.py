#!/usr/bin/python3
"""
log parsing
"""

import sys
import re


def output(log: dict) -> None:
    """
    helper function to display stats
    """
    print("File size: {}".format(log["file_size"]))
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code]:
            print("{}: {}".format(code, log["code_frequency"][code]))


if __name__ == "__main__":
    regex = re.compile(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+)\] "[A-Z]+ ([^"]+)" (\d+) (\d+)'
    )

    line_count = 0
    log = {}
    log["file_size"] = 0
    log["code_frequency"] = {}

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.match(line)
            if match:
                line_count += 1
                method = match.group(2)
                status_code = match.group(3)
                file_size = int(match.group(4))

                # File size
                log["file_size"] += file_size

                # Status code
                log["code_frequency"].setdefault(status_code, 0)
                log["code_frequency"][status_code] += 1

                if line_count % 10 == 0:
                    output(log)
    except KeyboardInterrupt:
        pass  # Allow graceful exit if interrupted
    finally:
        output(log)

