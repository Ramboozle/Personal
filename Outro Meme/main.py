import vlc,time,os
outro = vlc.MediaPlayer("TheFatRat-Xenogenesis.mp3")
outro.play()
outro.set_time(47000)
time.sleep(11)
os.system("shutdown -h now")
outro.stop()
