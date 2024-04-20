# from PIL import Image
# from cryptography.fernet import Fernet
# import zipfile

# import os
# from os import listdir
# from os.path import isfile, join






# dir_list = os.walk("./")
# next(dir_list)
# dir_list = [x for x in dir_list]
# # print(dir_list)

# key = Fernet.generate_key()
# cipher = Fernet(key)

# with zipfile.ZipFile('data', 'w') as zipf:
#     for i in dir_list:

#         path = i[0]
#         onlyfiles = i[2]

#         # Create a zip file to pack and encrypt image files
#         for i in onlyfiles:
#             # if(i[-4:] != ".png" or i[-4:] != ".jpg"): continue
#             img = Image.open(path + "/" +i)
#             img_bytes = img.tobytes()

#             # Encrypt image data
#             encrypted_img_bytes = cipher.encrypt(img_bytes)
#             zipf.writestr(f'{path[2:]}/image_{i[:-4]}.enc', img_bytes)

#             print(f'{path[2:]}/image_{i[:-4]}.enc')
#             # Save encryption key

#     zipf.writestr('key', key)


import zipfile
import os

def compress_images(directory, output_file):
    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(('.jpg', '.jpeg', '.png')):
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, arcname=os.path.relpath(file_path, directory))

compress_images('./', 'data')



from PIL import Image
def decompress_images(zip_file):
    with zipfile.ZipFile(zip_file, 'r') as zipf:
        return {info.filename: Image.open(zipf.open(info)) for info in zipf.infolist() if info.filename.endswith(('.jpg', '.jpeg', '.png'))}

image_dict = decompress_images('./data')

print(image_dict)

