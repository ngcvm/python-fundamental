import os
import csv

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

def check_file_exists(filename):
    return os.path.exists(os.path.joint(CURRENT_DIR, filename))

def file_path(filename):
    return os.getcwd() + '\\bai11\\' + filename

def read_report_file(filename):
    try:
        file_dir = os.getcwd() + '\\bai11\\' + filename
        file = open(file_dir, 'r', encoding='utf-8')
        content = file.read()
        print('File content: \n', content)
        print('Number of rows: ', len(content.split('\n')))
        print('Number of words: ', len(content.split()))
        print('Number of chars: ', len(content))
        file.close()
    except Exception as error:
        raise error

def read_file(filename):
    file_dir = os.getcwd() + '\\bai11\\' + filename
    if os.path.exists(file_dir):
        file = open(file_dir, 'r', encoding='utf-8')
        content = file.read()
        file.close()
        return content
    else:
        raise Exception('File not exists')

def write_file(filename, content):
    file_dir = os.getcwd() + '\\bai11\\' + filename
    file = open(file_dir, 'a', encoding='utf-8')
    file.write(content)
    file.close()
    print ('Content have been writed to filename: ', filename)


def read_csv(filename):
    file_dir = os.getcwd() + '\\bai11\\' + filename
    file = open(file_dir, 'r', encoding='utf-8')
    for row in csv.reader(file):
        print(row)
    file.close()

def write_csv(filename, content):
    file_dir = os.getcwd() + '\\bai11\\' + filename
    file = open(file_dir, 'w', newline='', encoding='utf-8')
    csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL).writerows(content)
    file.close()

def read_telephobe_csv(filename):
    file_dir = os.getcwd() + '\\bai11\\' + filename
    file = open(file_dir, 'r', encoding='utf-8')
    print('name\tphone')
    for name, phone in csv.reader(file):
        print(name + "\t" + phone)
    file.close()