
---

### **main.py**
```python
import random

def load_quotes(file_path):
    """Load quotes from a file and return them as a list."""
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def get_random_quote(quotes):
    """Return a random quote from the list."""
    return random.choice(quotes)

if __name__ == "__main__":
    quotes = load_quotes("quotes.txt")
    print("\n💡 Your motivational quote of the day:")
    print(f"\"{get_random_quote(quotes)}\"\n")
