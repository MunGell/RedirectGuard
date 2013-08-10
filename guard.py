import sys
import csv
import time
import os.path
import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument('--root', help="root URL to prepend to redirects URI")
parser.add_argument('--input', help="input file with URLs to check")
parser.add_argument('--output', help="output file with missing redirects")
args = parser.parse_args()

def read_input_file(input_file_path):
  redirects = []
  input_file = open(input_file_path, 'r')
  try:
    reader = csv.reader(input_file)
    for row in reader:
      redirects.append(row)
  finally:
    input_file.close()
  return redirects

def crawler(redirects):
  root = '' if not args.root else args.root
  for redirect in redirects:
    r = requests.get(root + redirect[0], allow_redirects=False)
    if r.status_code in [301, 302] and r.headers['location'] == ( root + redirect[1] ):
      print '[success] Redirect from ', redirect[0], ' to ', redirect[1], ' is successful with response code: ', str(r.status_code)
    else:
      location = r.headers['location'] if 'location' in r.headers else ''
      output(redirect, r.status_code, location)
    time.sleep(1)


def output(redirect, status, real_path):
  output_file  = open(args.output, "a")
  writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
  writer.writerow([redirect[0], redirect[1], status, real_path])
  output_file.close()


if __name__ == '__main__':
  # Check if input file exists
  if not os.path.isfile(args.input):
    print 'Input file does not exist.'
    exit()

  # Clear output file and add headers
  output_file  = open(args.output, "w+")
  writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
  writer.writerow(['Source', 'Target', 'Status code', 'Real target'])
  output_file.close()

  redirects = read_input_file(args.input)
  crawler(redirects)