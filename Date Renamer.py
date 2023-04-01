print('this file can cause some damage if used in the incorrect place. type "yes" to continue')
if input != yes:
  break

import datetime
import pathlib
for i in pathlib.Path().iterdir():
  print(i)
  print(i.suffix)
  suf=i.suffix
  tim=i.stat().st_ctime
  dattim=datetime.datetime.fromtimestamp(tim)
  print(dattim)
  i.rename(str(dattim)+suf)
