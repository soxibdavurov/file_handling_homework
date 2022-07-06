def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    number_of_characters = len(data)
    return number_of_characters
file = open("txt_file/data02.txt", "r")
data = file.read()
print(main(data))
# Read data from file
