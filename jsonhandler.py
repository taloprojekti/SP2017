from json import load, JSONDecoder, JSONDecodeError
def importJSON(filedir):
    try:
        data = load(open(filedir,'r', encoding='utf-8'))
    
        return data

    except JSONDecodeError:
        print('\033[31m' + "Error: " + '\033[0m' + "Failed to read the data file")
    return False
