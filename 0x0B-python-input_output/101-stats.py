#!/usr/bin/python3
import sys
import signal


def signal_handler(signal, frame):
    print_statistics()
    sys.exit(0)


def print_statistics():
    try:
        print("Total file size:", total_file_size)
        for status_code in sorted(status_codes):
            print(f"{status_code}: {status_codes[status_code]}")
        sys.stdout.flush()  # Flush the buffer to avoid BrokenPipeError
    except BrokenPipeError:
        pass  # Ignore BrokenPipeError when writing to a closed pipe


def process_line(line):
    global total_file_size
    global line_count
    global status_codes

    try:
        _, _, _, status_code, file_size = line.split(" ")[-5:]
        file_size = int(file_size)
        status_code = int(status_code)

        total_file_size += file_size
        status_codes[status_code] = status_codes.get(status_code, 0) + 1

        line_count += 1
        if line_count % 10 == 0:
            print_statistics()

    except ValueError:
        pass  # Ignore lines that do not conform to the expected format


def main():
    signal.signal(signal.SIGINT, signal_handler)

    global total_file_size
    global line_count
    global status_codes

    total_file_size = 0
    line_count = 0
    status_codes = {}

    try:
        for line in sys.stdin:
            process_line(line)
    except KeyboardInterrupt:
        pass  # Handle keyboard interruption

    print_statistics()


if __name__ == "__main__":
    main()
