# import os  # readflie , handing folder , path 
# import time   # loop 
# import shutil   # shell utilities   = move file , copy file , delete file 



# home = os.path.expanduser("~")

# for folder in os.listdir(home):
#     print(folder)

# DOWNLOADS= r"D:\learn python" 


# FOLDERS = {
#     "pdf" : "Documents", 
#     "docx" : "Documents" , 
#     "jpg" : "Images" , 
#     "jpeg" : "Images"   , 
#     "png" : "Images" , 
#     "mp3" :  "Music"
# }  


# def organize_file(filename) :
#     file_path = os.path.join(DOWNLOADS , filename)

#     if not os.path.isfile(file_path):
#         return 
    
#     ext  = filename.spilt(".")[-1].lower()
        
#     folder_name = FOLDERS.get(ext , "Others")
#     target_folder = os.path.join(DOWNLOADS, folder_name)
    

#     if not os.path.exists(target_folder ):
#         os.makedirs(target_folder)



#     new_path = os.path.join(target_folder , filename)
    

#     counter =1 
#     while os.path.exists(new_path): 
#         name , ext_full  = os.path.splitext(filename)
#         new_path = os.path.join(target_folder , f"{name}({counter}){ext_full}")

#         counter +=1 


#     shutil.move(file_path  , new_path)

#     print(f"Moved: {filename} -> {folder_name}")


# def watch_folder(): 
#     seen_file = set() 

#     while True :
#         files = os.listdir(DOWNLOADS) 

#         for file in files :
#             if file not in seen_file: 
#                 organize_file(file) 
#                 seen_file.add(file) 

        
#         time.sleep(3)




# watch_folder()


# print("Hello wo ")



import os     # readflie , handing folder , path 
    
import time  # loop 
 
import shutil  # shell utilities   = move file , copy file , delete file

# ใช้ path นี้ (แก้ให้ตรงของคุณได้)
DOWNLOADS = r"D:\learn python"   # r readonly text ไม่ต้องสน / 

# rule แยกไฟล์
FOLDERS = {    # map
    "pdf": "Documents",
    "docx": "Documents",
    "jpg": "Images",
    "jpeg": "Images",
    "png": "Images",
    "mp3": "Music"
}


def organize_file(filename):
    file_path = os.path.join(DOWNLOADS, filename)   #combine path = folder\file

    # ข้ามถ้าไม่ใช่ไฟล์ (เช่น folder)
    if not os.path.isfile(file_path):  # if not file = stop
        return

    # กันไฟล์ไม่มีนามสกุล
    if "." not in filename:
        ext = ""
    else:
        ext = filename.split(".")[-1].lower()   # ดึงนามสกุลของไฟล์

    # หา folder ปลายทาง
    folder_name = FOLDERS.get(ext, "Others")  # if true  foldername = ext  else foldername = "Others"
    target_folder = os.path.join(DOWNLOADS, folder_name)

    # สร้าง folder ถ้ายังไม่มี
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    new_path = os.path.join(target_folder, filename)

    # กันชื่อไฟล์ซ้ำ
    counter = 1
    while os.path.exists(new_path):
        name, ext_full = os.path.splitext(filename)
        new_path = os.path.join(target_folder, f"{name}({counter}){ext_full}")
        counter += 1

    # ย้ายไฟล์
    shutil.move(file_path, new_path)

    print(f"Moved: {filename} -> {folder_name}")


def watch_folder():
    seen_files = set()

    print("👀 Watching folder...")

    while True:
        files = os.listdir(DOWNLOADS)

        for file in files:
            if file not in seen_files:
                organize_file(file)
                seen_files.add(file)

        time.sleep(2)


# เริ่มโปรแกรม
watch_folder()