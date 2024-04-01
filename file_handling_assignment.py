try:
    # File Creation
    with open('my_file.txt', 'w') as file:
        file.write("First line of text\n")
        file.write("Second line with numbers: 12345\n")
        file.write("Third line with a mix of strings and numbers: Python 3.9\n")

    # File Reading and Display
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print("Content of my_file.txt:")
        print(content)

    # File Appending
    with open('my_file.txt', 'a') as file:
        file.write("Fourth line added in append mode\n")
        file.write("Fifth line appended with more text\n")
        file.write("Sixth line appended with additional content\n")

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

finally:
    print("Execution completed.")
