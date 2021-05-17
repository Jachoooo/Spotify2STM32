import spotipy
import time
import os
import serial
from spotipy.oauth2 import SpotifyOAuth

LCD_SIZE=20

f=open("pass.txt","r")
lines=f.readlines()
_id=lines[0].strip()
_secret=lines[1]
f.close()


scope="user-read-currently-playing"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=_id,
                                               client_secret=_secret,
                                               redirect_uri='http://example.com',
                                               scope = scope))

ser = serial.Serial('COM3')
scroll1=0
scroll2=0
while True:
    
    
    results = sp.current_user_playing_track()
    output1=''
    output2=''
    if results==None:
        break
    if results['is_playing']:
        output1+="Now Playing         "
    else:
        output1+="Paused              "
    artist=results['item']['artists'][0]['name'].ljust(LCD_SIZE, ' ')
    if(len(artist)>20):
        artist="   "+artist+"   "
        if scroll1+20>=len(artist):
            scroll1=0
        else:
            scroll1+=1

        artist=artist[0+scroll1:20+scroll1]
    output2+=artist
    
    song=results['item']['name'].ljust(LCD_SIZE, ' ')
    if(len(song)>20):
        song="   "+song+"   "
        if scroll2+20>=len(song):
            scroll2=0
        else:
            scroll2+=1

        song=song[0+scroll2:20+scroll2]
    output1+=song
    for i in range(0,LCD_SIZE):
        progress=int(LCD_SIZE*results['progress_ms']/results['item']['duration_ms'])
        if(progress>i):
            output2+='#'
        else:
            output2+=' '
        #print(int(100*results['progress_ms']/results['item']['duration_ms']))
    
    
    output1+=' '
    output2+=' '
    ser.write(output1.encode())
    time.sleep(1)
    ser.write(output2.encode())
    time.sleep(1)
    