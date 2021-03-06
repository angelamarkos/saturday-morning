import shutil
import os
import pwd
import grp
# shutil.copy2('./original.txt', './copy_original_metadata.txt')
# f = open('original.txt', 'r')
# f2 = open('copy_file.txt', 'w')
#
# shutil.copyfileobj(f, f2)

# f.close()
# f2.close()
#  ==========================================================
# shutil.copystat('./root_original.txt', './original.txt')
# print(os.stat('./root_original.txt'))
# print(os.stat('./original.txt'))
#
# print(os.stat('./root_original.txt').st_gid)
# os.chown('./original.txt',
#          os.stat('./root_original.txt').st_uid ,os.stat('./root_original.txt').st_gid)
#
# shutil.copymode('./original.txt', 'copies/copy_2/copy_original.txt')

# =========================================================
# os.rmdir('./copies')
# shutil.rmtree('./copies')

shutil.make_archive('./../archive_06_03_21', 'zip')
shutil.unpack_archive('./../archive_06_03_21.zip', './temp_dir')

