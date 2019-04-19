
def importJSON(filedir):
    from json import load, JSONDecoder, JSONDecodeError
    try:
        data = load(open(filedir,'r', encoding='utf-8'))
    
        return data

    except JSONDecodeError:
        print('\033[31m' + "Error: " + '\033[0m' + "Failed to read the data file")
    return False

def writeJSON(filedir, data):
    from json import dumps, JSONEncoder
    json_data = dumps(data)
    file = open(filedir, 'w', encoding='utf-8')
    file.write(json_data)

    return 1
