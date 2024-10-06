# bookbot
# Book Text Analysis Project

## Overview

This project analyzes the text of **Mary Shelley's _Frankenstein_** by counting the total number of words and the frequency of each character in the book. The script reads the book from a text file and generates a report detailing the word count and the frequency of each alphabetic character found in the document.

## Features

- **Word Counting:** The program computes the total number of words in the book.
- **Character Frequency:** It calculates the frequency of each letter (case-insensitive) in the text.
- **Report Generation:** A readable report is printed to the console showing the word count and character frequency, sorted by the most frequently occurring letters.

## Project Structure

```bash
.
├── books
│   └── frankenstein.txt  # Text file of Frankenstein
├── main.py               # Main script that executes the analysis
└── README.md             # Project documentation (this file)
```

- `books/frankenstein.txt`: The text file containing the content of the book to analyze.
- `main.py`: The main Python script that performs the analysis and prints the report.
- `README.md`: Documentation file explaining the project.

## How It Works

1. **Read the Book**: The program reads the text file containing _Frankenstein_ using the `read_file` function.
2. **Count Words**: The `count_words` function splits the content into words and counts how many words are present.
3. **Count Characters**: The `count_characters` function counts the frequency of each alphabetic character in the book, ignoring case and non-alphabetic characters.
4. **Generate Report**: The `print_report` function generates a report showing the total word count and the frequency of each letter, sorted in descending order of frequency.

## Usage

### Prerequisites
- Python 3.x installed on your system.

### Steps to Run the Project:

1. Clone or download this repository.
2. Ensure that the book file `frankenstein.txt` is placed in the `books` directory.
3. Run the `main.py` script:

   ```bash
   python main.py
   ```

### Example Output:

```
--- Begin report of books/frankenstein.txt ---

40023 words found in the document.

The 'e' character was found 20345 times
The 't' character was found 15032 times
The 'a' character was found 13045 times
...

--- End report ---
```

## Customization

If you'd like to analyze a different book or text file, replace the `frankenstein.txt` file in the `books` directory with your desired text file and ensure the file path in `read_file()` points to it.

## Future Improvements

- Add support for handling multiple text files.
- Extend character analysis to include digits and punctuation.
- Save the generated report to a file for further analysis.


---

Feel free to modify the text file or script to suit your needs. Happy analyzing!
