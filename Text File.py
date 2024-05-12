def find_unique_words(filename):
  try:
    # Open the file in read mode
    with open(filename, 'r') as file:
      # Read the entire file content
      text_content = file.read()

    # Convert text to lowercase and split into words
    words = text_content.lower().split()

    # Use set to remove duplicates and preserve order (optional)
    unique_words = set(words)  # Uncomment for unique words without order

    # Alternatively, use a dictionary to count word occurrences (optional)
    # word_counts = {}
    # for word in words:
    #   word_counts[word] = word_counts.get(word, 0) + 1
    # unique_words = [word for word, count in word_counts.items() if count == 1]

    # Print the unique words (or comment out for word counts)
    for word in unique_words:
      print(word)

  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

# Example usage
filename = "your_text_file.txt"  # Replace with your actual file name
find_unique_words(filename)
