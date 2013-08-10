# Redirect Guard

## Description

This very small command line tool that is written for checking redirects on a given website and produce a report on which redirects are not working or working incorrectly.

## Requirements

This program is written in Python and tested on version 2.7.5, however it might work on other versions as well.
All the requirements in terms of Python modules are in requirements.txt file and easy to install by following command:

`pip install -r requirements.txt`

## Usage

The script accepts three parameters:

* `--input` points the input CSV file with two columns: source and target URLs.
* `--output` points the output file with all broken redirects. It will be created if not presented in the system.
* `--root` sets root domain/directory for all the links in the input file, which will be prepended to every redirect URL

Example command:

`python guard.py --input input.csv --output output.csv`

## CSV format

### Input file

Input file should be in CSV format presenting two columns – first is for source URL and second is for target URL. Please remove headers of these columns as the script is not smart enough (for now) to skip them.

Example file:

```
"http://twitter.github.com/bootstrap/","http://twitter.github.io/"
"http://twitter.github.com/bootstrap/getting-started.html","http://twitter.github.io/bootstrap/getting-started.html"
"http://twitter.github.com/bootstrap/scaffolding.html","http://twitter.github.io/bootstrap/scaffolding.html"
"http://twitter.github.com/bootstrap/components.html","http://twitter.github.io/bootstrap/components.html"
```

### Output file

All the missing or broken redirects are written to output file in CSV format. Output presents given source and target URLs, response status code and the real URL of redirection (if any).

Example file:

```
"Source","Target","Status code","Real target"
"http://google.com","http://google.com","301","http://www.google.com/"
"http://twitter.github.com/bootstrap/","http://twitter.com","301","http://twitter.github.io/bootstrap/"
```

## License

This several lines of code (the script) are distributed under BSD 2-Clause license.