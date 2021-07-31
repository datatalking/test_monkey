#!/usr/bin/python
import os
import sys
import csv
import datetime
import time


def main():
	run_simple_speedtest()
	check_network_connection()


def run_simple_speedtest():
	"""
	A function using speedtest-cli
	"""
	# run speedtest - cli
	print('running test')
	speed = os.popen("speedtest-cli --simple").read()
	print('done')
	
	# split the 3 line result (ping,down and up)
	lines = speed.split('\n')
	print(speed)
	
	ts = time.time()
	now = time.strftime('%d-%m-%Y %H:%M:%S')
	# if speedtest could not connect set the speeds to 0
	if "Cannot" in speed:
		p = 0
		d = 0
		u = 0
	# extract the values for ping, down and up values
	else:
		p = lines[0][6:11]
		d = lines[1][10:16]
		u = lines[2][8:12]
	print(now, p, d, u)
	# save the data to a csv
	out_file = open('speed.csv', 'a')
	writer = csv.writer(out_file)
	writer.writerow((now, p, d, u))
	out_file.close()


def check_network_connection():
	"""
	A function to ping network connection to ensure when functions run network is active, else function doesn't run
	"""
	pass


if __name__ == '__main__':
	main()
