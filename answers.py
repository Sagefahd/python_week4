def read_and_write_file(input_filename, output_filename):
    try:
        
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        
        modified_content = content.upper()  
        
        
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Content from {input_filename} has been successfully modified and written to {output_filename}.")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except IOError:
        print(f"Error: An error occurred while reading or writing to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


input_file = input("Enter the name of the file to read from: ")
output_file = input("Enter the name of the file to write to: ")


read_and_write_file(input_file, output_file)
