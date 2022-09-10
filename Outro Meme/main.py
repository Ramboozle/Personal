import vlc,time,os
outro = vlc.MediaPlayer("TheFatRat-Xenogenesis.mp3")
outro.play()
outro.set_time(47000)
time.sleep(9.5)
os.system("shutdown -h now") #will not work and needs SU :(
time.sleep(5) #if I could get it to run in SU I would time it better 
outro.stop()
