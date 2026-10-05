# Week 6 Assignment - Safe Functions

- `safe_tools.py` - Contains three functions that safely handle division, number conversion, and dictionary lookups.
- `unbreakable.py` - Contains the unbreakable program for the assignment.
- `README.md` - Describes the files and explains why an if check cannot catch invalid number conversion.

An if check cannot catch "abc" on its own because the error happens when Python tries to convert "abc" into an integer using int(). The ValueError must be handled with try/except.
