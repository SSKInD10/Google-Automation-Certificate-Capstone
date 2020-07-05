#!/usr/bin/env python3
import os,emails
import psutil,shutil,socket

def send_email(subject):
	sender = "automation@example.com"
	receiver = "{}@example.com".format(os.environ.get("USER"))
	body = "Please check your system and resolve the issue as soon as possible"
	message = emails.generate(sender,receiver,subject,body,None)
	emails.send(message)
def check_disk_space():
	storage = shutil.disk_usage(os.getcwd())
	if storage.used/storage.total > 0.8:
		subject = "Error - Available disk space is less than 20%"
		send_email(subject)
def check_cpu_load():
	cpu_per = psutil.cpu_percent(interval = 0.5)
	if cpu_per > 0.8:
		subject = "Error - CPU usage is over 80%"
		send_email(subject)
def check_ram_usage():
	ram_usage = psutil.virtual_memory()
	if ram_usage.available < 500*1024*1024:
		subject = "Error - Available memory is less than 500MB"
		send_email(subject)
def check_localhost():
	try:
		resolver = socket.gethostbyname('localhost')
	except:
		subject = "Error - localhost cannot be resolved to 127.0.0.1"
		send_email(subject)
if __name__ == "__main__":
	check_disk_space()
	check_cpu_load()
	check_ram_usage()
	check_localhost()
