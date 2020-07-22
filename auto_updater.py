from datetime import datetime, timedelta
from threading import Timer
from shutil import copyfile
import os
import pandas as pd

# This script is for updaing main Db, runs everyday at 12:00am  
# This checks main db files with updated db files, if there are any updates, updated files are replaced with main db files

def auto_updater():
	src = "updated/"
	dst = "new_database/"
	logs_file = "logs.txt"
	file = open(logs_file, 'a')

	for path in os.listdir(dst):
		
		src_path = os.path.join(src, path)
		dst_path = os.path.join(dst, path)

		if path == "python.csv":
			df = pd.read_csv(dst_path)
			df_python = pd.read_csv(src_path)
			if df.equals(df_python):
				file.write(str(datetime.now()) + " No change detected in "+ path + "\n")
				file.write("\n")
			else:
				copyfile(src_path, dst_path)
				file.write(str(datetime.now()) + " Updates in "+ path + "\n")
				file.write("\n")

		if path == "nodeJS.csv":
			
			df = pd.read_csv("new_database/nodeJS.csv")
			df_nodejs = pd.read_csv(src_path)
			if df.equals(df_nodejs):
				file.write(str(datetime.now()) + " No change detected in "+ path + "\n")
			else:
				copyfile(src_path, dst_path)
				file.write(str(datetime.now()) + " Updates in "+ path + "\n")

		if path == "cpp.csv":
			df = pd.read_csv(dst_path)
			df_cpp = pd.read_csv(src_path)
			if df.equals(df_cpp):
				file.write(str(datetime.now()) + " No change detected in "+ path + "\n")
			else:
				copyfile(src_path, dst_path)
				file.write(str(datetime.now()) + " Updates in "+ path + "\n")

		if path == "html.csv":
			df = pd.read_csv(dst_path)
			df_html = pd.read_csv(src_path)
			if df.equals(df_html):
				file.write(str(datetime.now()) + " No change detected in "+ path + "\n")
			else:
				copyfile(src_path, dst_path)
				file.write(str(datetime.now()) + " Updates in "+ path + "\n")

	file.close()
	x = datetime.today()
	y = x.replace(day=x.day, hour=0, minute=0, second=1, microsecond=0)

	delta_t = y-x

	secs = delta_t.total_seconds()

	if secs < 0:
		secs += timedelta(days=1).total_seconds()

	display = str(timedelta(seconds = secs)).split(".")[0]
	

	t = Timer(secs, auto_updater)
	print(t)
	print("*** Database Updated ***")
	print("next update in "+ (display) +"\n")
	t.start()

auto_updater()