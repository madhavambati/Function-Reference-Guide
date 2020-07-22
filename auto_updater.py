from datetime import datetime, timedelta
from threading import Timer
from shutil import copyfile
import os
import pandas as pd

def auto_updater():
	src = "updated/"
	dst = "new_database/"
	logs = ""
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
	x=datetime.today()
	y = x.replace(day=x.day, hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
	delta_t=y-x
	print("next update in "+ str(delta_t)+"\n")
	secs=delta_t.total_seconds()
	t = Timer(secs, auto_updater)
	t.start()



auto_updater()