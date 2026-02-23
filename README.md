# SecurePasswordGenerator (Python + Tkinter)

A lightweight **desktop password generator** built with **Python** and **Tkinter**. Users enter a desired password length (minimum **8** characters), click **Generate**, and the app produces a randomized password that includes a mix of **letters, numbers, and symbols**. A **Copy to Clipboard** button makes it easy to paste the password into other apps.

## Features

### Current Features
- Simple **Tkinter desktop GUI**
- User-defined password length with validation (**minimum 8 characters**)
- Generates passwords using a mix of:
  - letters (uppercase + lowercase)
  - numbers
  - symbols
- Ensures each generated password includes **at least one letter, one number, and one symbol**
- Shuffles characters to reduce predictable patterns
- **Copy to Clipboard** button with confirmation message

### Planned Features
- Character-type selection with checkboxes:
  - Include Uppercase
  - Include Lowercase
  - Include Numbers
  - Include Symbols
- **Show/Hide password** toggle in the UI
- Option to switch to `secrets` for stronger randomness
- Password strength indicator and additional customization options

## How It Works
1. Enter a password length (8 or more).
2. Click **Generate** to create a password.
3. Click **Copy to Clipboard** to copy it for use elsewhere.

## Requirements
- Python 3.x
- No third-party dependencies (uses Python standard library + Tkinter)

## Run Locally
Clone the repo:
   ```bash
git clone https://github.com/johannesbreur/SecurePasswordGenerator.git

cd SecurePasswordGenerator
