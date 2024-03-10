def main():
    filename = input("Enter the name of the text file: ")
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total_words = 0
            total_chars = 0
            for line in lines:
                words = line.split()
                total_words += len(words)
                total_chars += sum(len(word) for word in words)
            num_lines = len(lines)
            avg_words_per_line = total_words / num_lines if num_lines else 0
            avg_chars_per_word = total_chars / total_words if total_words else 0
            print(f"Number of lines: {num_lines}")
            print(f"Average number of words per line: {avg_words_per_line}")
            print(f"Average number of characters per word: {avg_chars_per_word}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
if __name__ == "__main__":
    main()
