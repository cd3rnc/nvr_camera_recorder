import os


def file_size(file_path):
    file_size = os.path.getsize(file_path)
    #print("the file size in MBytes: ",round(file_size/1024/1024,2)," Mbytes")
    return file_size

