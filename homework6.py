song='''
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky. Twinkle,
twinkle, little star,
How I wonder what you are!
When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.
'''
song=song.lower()
song=song.replace('\n',' ')
song=song.replace(',',' ')
song=song.replace('.',' ')
song=song.replace('!',' ')
song=song.split()
print(song)
song_1={}
for i in song:
    if i not in song_1:
        song_1[i]=1
    else:
        song_1[i]+=1
for a,b in song_1.items():
    print(f'{a}出现了{b}次')
