📄 Project Description
This project is a Python program that reads a text file and counts the occurrences of each word in the file. The results are displayed in alphabetical order along with their respective counts. It is a simple yet practical example of text processing and file handling in Python.

🛠️ Features
Reads a text file and processes its content.
Counts the occurrences of each word.
Displays the results in alphabetical order.
Ignores case sensitivity while counting words.

📁 File Structure
│── filemanipulation.py
│── sample_text.txt
│── README.md
word_frequency_counter.py: The main Python program.
sample_text.txt: Example text file for testing.

📄 Example Output
Suppose sample_text.txt contains the following content:
Hello world! This is a sample text file.
This file is for counting word occurrences.
Hello world!

The output will be:
a: 1
counting: 1
file: 2
for: 1
hello: 2
is: 2
occurrences: 1
sample: 1
text: 1
this: 2
word: 1
world: 2

🛡️ Note
The program ignores punctuation marks while counting words.
It is case-insensitive, treating 'Hello' and 'hello' as the same word.

💡 Future Improvements
Support for multiple text files.
Option to save the output to a new file.
Enhanced text cleaning and preprocessing.
