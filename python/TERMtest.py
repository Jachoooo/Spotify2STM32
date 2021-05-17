import spotipy
import time
import os
from spotipy.oauth2 import SpotifyOAuth

PROGRESSBAR_LENGTH=40

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
os.system('cls')
while True:
    
    #os.system('cls')
    results = sp.current_user_playing_track()
    output=''
    if results==None:
        break
    if results['is_playing']:
        output+="Now Playing\n"
    else:
        output+="Paused     \n"
    output+=results['item']['artists'][0]['name'].ljust(PROGRESSBAR_LENGTH+2, ' ')
    output+="\n"
    output+=results['item']['name'].ljust(PROGRESSBAR_LENGTH+2, ' ')
    output+="\n"
    output+='['
    for i in range(0,PROGRESSBAR_LENGTH):
        progress=int(PROGRESSBAR_LENGTH*results['progress_ms']/results['item']['duration_ms'])
        if(progress>i):
            output+='#'
        else:
            output+=' '
        #print(int(100*results['progress_ms']/results['item']['duration_ms']))
    output+=']\n'
    print("\033[?25l")
    print("\033[H")
    print(output)
    time.sleep(1)
    