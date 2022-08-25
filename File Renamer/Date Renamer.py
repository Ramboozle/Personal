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