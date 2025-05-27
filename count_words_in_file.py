def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            print(f" The file '{filename}' contains {word_count} words.")
    except FileNotFoundError:
        print(f" Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")

# Example usage
filename = input("Enter the file name (with extension): ")
count_words_in_file(filename)
