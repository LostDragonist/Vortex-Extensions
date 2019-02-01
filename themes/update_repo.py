import shutil
import os

THEME_LIST = (
  "More Information",
  )

VORTEX_DIR = os.path.expandvars(r'%APPDATA%\Vortex\themes')

for theme in THEME_LIST:
  src_path = os.path.join(VORTEX_DIR, theme)
  dst_path = os.path.join(os.getcwd(), theme)
  if not os.path.exists(src_path):
    print('Theme not found at "{}". Skipping...'.format(src_dst))
  if os.path.exists(dst_path):
    print('Removing "{}"'.format(dst_path))
    shutil.rmtree(dst_path)
  print('Copying "{}" to "{}"'.format(src_path, dst_path))
  shutil.copytree(src_path, dst_path)

input('Press enter to continue...')
