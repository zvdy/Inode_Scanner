import os
import sys
import argparse

# Usage: python3 inode_scanner.py -f /path/to/file

def main():
    parser = argparse.ArgumentParser()
    # Make -p optional to specify a path to scan
    parser.add_argument('-p', '--path', help='Path to scan')
    # Make -f not optional to specify a file to scan
    parser.add_argument('-f', '--file', help='File to scan', required=True)
    args = parser.parse_args()

    # Check if the file exists
    if not os.path.isfile(args.file):
        print('File does not exist')
        sys.exit(1)

    # Check if the path exists
    if args.path and not os.path.isdir(args.path):
        print('Path does not exist')
        sys.exit(1)

    # Get the inode number of the file
    inode = os.stat(args.file).st_ino

    # If a path is specified, scan that path
    if args.path:
        path = args.path
    # Otherwise, scan root directory
    else:
        path = '/'
    # Scan the path for files with the same inode number
    for root, dirs, files in os.walk(path):
        for file in files:
            # Get the full path of the file
            file_path = os.path.join(root, file)
            # Check if the file has the same inode number
            if os.stat(file_path).st_ino == inode:
                print(file_path)


if __name__ == '__main__':
    main()