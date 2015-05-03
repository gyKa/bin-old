import os
import shutil
from datetime import date

directories = {
    '/home/gytis/Desktop': 'Desktop',
    '/home/gytis/Documents': 'Documents',
    '/home/gytis/Downloads': 'Downloads',
    '/home/gytis/Music': 'Music',
    '/home/gytis/ownCloud': 'ownCloud',
    '/home/gytis/Pictures': 'Pictures',
    '/home/gytis/Public': 'Public',
    '/home/gytis/Templates': 'Templates',
    '/home/gytis/Videos': 'Videos',
    '/home/gytis/Workspace': 'Workspace',
}

external_disk_path = '/media/gytis/HTPC'

storage_mount_error = 'Your storage is not mounted!'
storage_mount_success = 'Your backup is ready!'
message = ''

if os.path.ismount(external_disk_path):
    message = storage_mount_success
    today = date.today()
    backup_directory = external_disk_path + '/backups/' + today.strftime("%Y%m%d")

    os.mkdir(backup_directory)

    for source_directory, source_name in directories.iteritems():
        shutil.copytree(source_directory, backup_directory + '/' + source_name)
else:
    message = storage_mount_error

notification_command = 'notify-send "%s"' % message

os.system(notification_command)
