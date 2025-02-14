import re
import argparse
import datetime
from collections import Counter

def password_generator(file_path):
    """Generator that yields each password from the file line by line."""
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            yield line.strip()  # Yield one password at a time

def extract_numbers(password):
    """Extract all numeric sequences from a password."""
    return re.findall(r'\d+', password)

def analyze_passwords(file_path):
    """Analyze passwords and count number sequences using a generator."""
    number_counter = Counter()

    for password in password_generator(file_path):
        numbers = extract_numbers(password)
        number_counter.update(numbers)  # Update count for extracted numbers

    return number_counter

def save_results_to_file(file_path, number_counter, top_n):
    """Save results to a log file with a timestamped filename."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_filename = f"{file_path}_TopSequentialDigits_{timestamp}_log.txt"

    with open(output_filename, "w", encoding="utf-8") as out_file:
        out_file.write(f"Top {top_n} most common numeric sequences:\n\n")
        for num, count in number_counter.most_common(top_n):
            out_file.write(f"Number: {num}, Count: {count}\n")

    print(f"\nResults saved to: {output_filename}")

def save_results_to_hashcat_rules(number_counter, top_n):
    """Save results as a Hashcat rules file."""
    rules_filename = "TopSequentialDigits.rule"

    with open(rules_filename, "w", encoding="utf-8") as rules_file:
        for num, _ in number_counter.most_common(top_n):
            rule = "$" + "$".join(num)  # Convert "12345" to "$1$2$3$4$5"
            rules_file.write(rule + "\n")

    print(f"Hashcat rules saved to: {rules_filename}")

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Analyze most common numeric sequences in passwords.")
    parser.add_argument("file", help="Path to the password file")
    parser.add_argument("-n", "--top", type=int, default=20, help="Number of top results to display (default: 20)")
    parser.add_argument("--save", action="store_true", help="Save results to a timestamped log file")
    parser.add_argument("--rules", action="store_true", help="Save results as a Hashcat rules file")

    args = parser.parse_args()
    file_path = args.file
    top_n = args.top

    # Run analysis
    number_counter = analyze_passwords(file_path)

    # Print the most common numeric sequences
    print(f"\nTop {top_n} most common numeric sequences:\n")
    for num, count in number_counter.most_common(top_n):
        print(f"Number: {num}, Count: {count}")

    # Save results if the flag is set
    if args.save:
        save_results_to_file(file_path, number_counter, top_n)

    # Save as Hashcat rules file if the flag is set
    if args.rules:
        save_results_to_hashcat_rules(number_counter, top_n)

if __name__ == "__main__":
    main()
