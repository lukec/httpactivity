import json

filename = 'web/status.json'

def initialize():
    write_status({'command': 'idle'})

def read_status():
    fh = open(filename, 'r')
    content = fh.read()
    return json.read(content)

def write_status(opts):
    fh = open(filename, 'w')
    fh.write(json.write(opts))
    fh.close()

# For testing
if __name__ == '__main__':
    status = read()
    print "Command: %s"%status['command']
