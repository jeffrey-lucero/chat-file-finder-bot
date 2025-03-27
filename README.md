# Chatterbot File Finder Chatbot

## Overview
This Python chatbot uses ChatterBot for conversational AI and Google Translate for multi-language support. It can respond to user inquiries and search for files or folders on your computer.

## Features
- AI-powered chatbot with trained responses
- Multi-language support using Google Translate
- File and folder search functionality
- User-friendly console interface

## Requirements
- Python 3.x
- ChatterBot
- ChatterBotCorpusTrainer
- Googletrans

## Installation
1. Install Python 3 if not already installed.
2. Install the required dependencies:
   ```sh
   pip install chatterbot chatterbot_corpus googletrans==4.0.0-rc1
   ```
3. Run the chatbot script:
   ```sh
   python chatbot.py
   ```

## Usage
- Type your question, and the chatbot will respond.
- To search for a file or folder, type:
  ```
  Find [filename] in [directory]
  ```
  Example:
  ```
  Find report.pdf in C:\Users\Documents
  ```
- Type `exit` to close the chatbot.

## Notes
- The default search directory is `C:\vardump`.
- The chatbot may take time to search large directories.
- Permission errors may cause some directories to be skipped.

## License
This project is open-source and free to use. Modify and distribute as needed.
