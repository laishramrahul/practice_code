import os
fopen=open("new_wav.scp","r")
fwrite=open("fileName","a")
def get_filename_without_extension(file_path):
    file_name=os.path.basename(file_path)
    print(os.path.splitext(file_name)[0])
    fwrite.write(os.path.splitext(file_name)[0] +" "+file_path)

for eachline in fopen:
    get_filename_without_extension(eachline)
fopen.close()
fwrite.close()