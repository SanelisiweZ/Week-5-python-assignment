def read_file(filename):
    """Attempts to read the content of the given file."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found.")
    except IOError:
        print(f"❌ Error: Could not read the file '{filename}'.")
    return None

def write_file(filename, content):
    """Writes modified content to a new file."""
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"✅ Successfully wrote to '{filename}'")
    except IOError:
        print(f"❌ Error: Could not write to the file '{filename}'.")

def modify_content(content):
    """Modify the content in some way. Here, we convert it to uppercase."""
    return content.upper()

def main():
    # Ask user for input filename
    input_file = input("📄 Enter the name of the file to read: ")
    content = read_file(input_file)

    if content is not None:
        # Modify the content
        modified = modify_content(content)

        # Ask user for output filename
        output_file = input("💾 Enter the name of the new file to save the modified content: ")
        write_file(output_file, modified)

if __name__ == "__main__":
    main()
