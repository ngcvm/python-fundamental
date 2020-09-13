import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

def check_file_exists(filename):
    return os.path.exists(os.path.joint(CURRENT_DIR, filename))

def read_report_file(filename):
    file = open(os.path.join(CURRENT_DIR, filename), 'r')
    content = file.read()
    print('File content: \n', content)
    print('Number of rows: ', len(content.split('\n')))
    print('Number of words: ', len(content.split()))
    print('Number of chars: ', len(content))
    file.close()