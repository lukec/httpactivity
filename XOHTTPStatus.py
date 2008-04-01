import json

filename = 'web/status.json'

def read():
    fh = open(filename, 'r')
    content = fh.read()
    return json.read(content)


# For testing
if __name__ == '__main__':
    status = read()
    print "Command: %s"%status['command']
