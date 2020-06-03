import csv
import time
import os.path
import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument('input', help='input file with URLs to check')
parser.add_argument('--output', help='output file with missing redirects, default is results.csv', default='results.csv')
parser.add_argument('--root', help='root URL to prepend to redirects URI', default='')
parser.add_argument('--sleep', help='timeout between requests in seconds, default value is 1 second', type=int, default=1)
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
    timeout = 1 if not args.sleep else args.sleep

    results = []

    for redirect in redirects:
        link = root + redirect[0]
        expected_redirect = root + redirect[1]
        r = requests.get(link, allow_redirects=False)
        actual_redirect = '' if not 'location' in r.headers else r.headers['location']
        status_code = r.status_code
        result = status_code in [301, 302] and actual_redirect == expected_redirect
        results.append([link, expected_redirect, actual_redirect, status_code, result])
        time.sleep(timeout)

    return results


def save_data(rows):
    output_file = open(args.output, 'w+')
    writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(['Link', 'Expected Redirect', 'Actual Redirect', 'Status Code', 'Result'])
    writer.writerows(rows)
    output_file.close()


if __name__ == '__main__':
    # Check if input file exists
    if not os.path.isfile(args.input):
        print('Input file does not exist.')
        exit()

    redirects = read_input_file(args.input)
    results = crawler(redirects)
    save_data(results)
