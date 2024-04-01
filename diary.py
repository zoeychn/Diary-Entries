from datetime import datetime

def write_diary():
    print("Writing Diary Entry:")
    entry = input("Enter your diary entry for today:\n")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("diary.txt", "a") as file:
        file.write(f"{timestamp}\n{entry}\n\n")
    print("Diary entry saved successfully! See diary.txt to view your entries :)")

def read_diary():
    print("Reading Diary Entries:")
    try:
        with open("diary.txt", "r") as file:
            entries = file.read().strip().split('\n\n')
            if not entries:
                print("No diary entries found.")
            else:
                for i, entry in enumerate(entries, 1):
                    timestamp, content = entry.split('\n', 1)
                    print(f"Entry {i} - Date: {timestamp}:\n{content}")
    except FileNotFoundError:
        print("No diary entries found.")

def main():
    # Main function to run the diary program #
    while True:
        print("\nSelect option:")
        print("1. Write Diary Entry")
        print("2. Read Diary Entries")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ")

        if choice == '1':
            write_diary()
        elif choice == '2':
            read_diary()
        elif choice == '3':
            print("Exiting the diary program. Goodbye!")
            break
        else:
            print("Invalid input. Please enter a valid option.")

if __name__ == "__main__":
    main()
