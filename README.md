# Bulk Goodreads Adder

This project contains a Python script that reads a text file, searches for books on Goodreads, and adds them to your "Want to Read" shelf.

## File Structure

- `goodreads.py`: The main script that performs the text parsing and formatting.
- `books.txt`: The text file containing a list of books to be added to Goodreads. Add each of your books on a new line.

## How to Run

1. Ensure you have Python installed on your system.
2. Install the neccessary requirements by running the following command: `pip install -r requirements.txt`.
3. Place the texte file for the books you want to search for in the same directory as `goodreads.py` and name it `books.txt`.
4. Run the `goodreads.py` script with Python:

```python
python Parser.py
```
