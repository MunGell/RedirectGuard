# Redirect Guard

## Description

A small command line tool to verify redirects on a given website. Uses CSV file as an input of links and their expected redirects and produces CSV report on their status.

## Requirements

This program is written in Python and tested on version 3, however it might work on other versions as well.

## Usage

The script accepts three parameters:

* `--output` specifies report file, will be created if not presented in the system or overridden otherwise
* `--root` sets root domain/directory, which will be prepended to every link in the input file, default is empty string
* `--sleep` specifies timeout (in seconds) between requests to avoid network issues, default is 1 second

Example command:

`python main.py example.csv`

## License

This several lines of code (the script) are distributed under BSD 2-Clause license.
