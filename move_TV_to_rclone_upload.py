#!/usr/bin/python

import os, shutil

dir1 = r'/mnt/user/Media/television'
dir2 = r'/mnt/user/mount_rclone/tdrive_media_vfs/television'
copy_dest = r'/mnt/user/rclone_upload/tdrive_media_vfs/television'

dir1_folders = [dir for dir in os.listdir(dir1) if os.path.isdir(os.path.join(dir1, dir))]
dir2_folders = [dir for dir in os.listdir(dir2) if os.path.isdir(os.path.join(dir2, dir))]

for dir in dir1_folders:
    if dir in dir2_folders:
        shutil.move(os.path.join(dir1, dir), os.path.join(copy_dest, dir))