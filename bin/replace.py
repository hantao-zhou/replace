#!/usr/bin/env python3

import re
import argparse

def replace_latex_syntax(input_file, output_file=None):
    if output_file is None:
        output_file = input_file
    try:
        with open(input_file, 'r') as file:
            content = file.read()

        # Replace \] and \[ with $$
        content = re.sub(r'\\\[', r'$$', content)
        content = re.sub(r'\\\]', r'$$', content)

        # Replace \( and \) with $
        content = re.sub(r'\\\( ', r'$', content)
        content = re.sub(r' \\\)', r'$', content)

        with open(output_file, 'w') as file:
            file.write(content)

        print(f"Replacements done. Updated content written to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Replace LaTeX syntax in a file.")
    parser.add_argument("input_file", help="Path to the input file.")
    parser.add_argument(
        "--output-file", 
        "-o",
        help="Path to the output file. If not provided, the input file will be overwritten.",
        default=None
    )
    args = parser.parse_args()

    replace_latex_syntax(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
