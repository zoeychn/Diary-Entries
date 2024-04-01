# Diary-Entries

This code provides a simple command-line interface for managing diary entries, allowing users to write new entries, read existing ones, and exit the program when done.

1. Functions:
   - `write_diary()`: This function allows the user to write a diary entry. It prompts the user to input their entry, records the current timestamp, and saves both the timestamp and the entry content to a file named `diary.txt`.
   - `read_diary()`: This function reads and displays all the diary entries stored in the `diary.txt` file. If no entries are found or if the file doesn't exist, it informs the user accordingly.
   - `main()`: This is the main function that runs the diary program. It displays a menu of options to the user, prompting them to either write a diary entry, read existing entries, or exit the program.

2. Main Program Logic:
   - The `main()` function is an infinite loop that continues until the user chooses to exit the program.
   - Inside the loop, it prints the menu of options and waits for the user to input their choice.
   - Depending on the user's choice, it calls the corresponding function (`write_diary()`, `read_diary()`, or exits the loop).

3. Execution Entry Point:
   - The `if __name__ == "__main__":` block ensures that the `main()` function is executed only when the script is run directly, not when it's imported as a module in another script. This is a common Python idiom to prevent code from running when importing modules.

4. User Interaction:
   - The program communicates with the user through the console. It prompts the user to input their choice and displays messages confirming actions such as saving a diary entry or exiting the program.

5. File Handling:
   - The program reads and writes diary entries to/from a file named `diary.txt`. It uses the `with open()` construct to ensure that the file is properly opened and closed, even if an error occurs during processing.
