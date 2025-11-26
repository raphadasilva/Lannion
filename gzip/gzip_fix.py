import gzip
import os

for file in os.listdir("zips"):
    print(file)
    with gzip.open(f"zips\\{file}", 'rb') as fg:
    	with open(f"data\\{file[:-3]}", 'wb') as f_out:
    		f_out.write(fg.read())
    		f_out.close()
