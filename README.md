# Password Analyzer: Top Digit Sequences

This project analyzes passwords to find the most common numeric sequences. It can also save the results to a log file or a Hashcat rules file.

## Pre-built Rules
Included in the repository are pre-built rules for the top 20, 50, 100, 200, 300 and 500 numeric sequences. These rules can be found in the `rules` directory. The rules are built from analyzing the "hashmob.net_2025-01-19.found.txt" password list. The rules are sorted by frequency, with the most common sequences appearing first.

NOTE: The data set anlyzed come from recovered passwords, but is deduplicated. This means that the frequency of a sequence may be higher than it would be in a real-world scenario. So this frequency analysis is among unique passwords.

## Features

- Analyze passwords from a file to find the most common numeric sequences.
- Display the top N most common numeric sequences.
- Save the results to a timestamped log file.
- Save the results as a Hashcat rules file.

## Requirements

- Python 3.x
- Required packages are listed in `requirements.txt`.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/Password-Analyzer-Top-Digit-Sequences.git
    cd Password-Analyzer-Top-Digit-Sequences
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To run the password analyzer, use the following command:

```sh
python analyze_passwords_digits.py <file> [-n TOP] [--save] [--rules]
```

### Arguments

- `file`: Path to the password file.
- `-n, --top`: Number of top results to display (default: 20).
- `--save`: Save results to a timestamped log file.
- `--rules`: Save results as a Hashcat rules file.

### Example

```sh
python analyze_passwords_digits.py passwords.txt -n 10 --save --rules
```

This command will analyze the passwords in `passwords.txt`, display the top 10 most common numeric sequences, save the results to a timestamped log file, and save the results as a Hashcat rules file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.