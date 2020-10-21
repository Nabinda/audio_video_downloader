# try:
#     from pytube import YouTube
#     from pytube import Playlist
# except Exception as e:
#     print("Errors:{}".format(e))

# url = "https://www.youtube.com/watch?v=m_7JMmBW-Zc"
# ytd = YouTube(url).streams.first().download()
# print(ytd)
import tkinter,sys
from pytube import YouTube
from pytube import Playlist

def dAudio():
    url = textField.get()
    ytd = YouTube(url.strip()).streams.filter(only_audio=True).first().download(output_path="D:/Downloads")
    print(ytd)

def dVideo():
    url = textField.get()
    ytd = YouTube(url).streams.order_by('resolution').desc().filter(file_extension="mp4",progressive=True).first().download(output_path="D:/Downloads")
    print(ytd)

win = tkinter.Tk()
win.title("Youtube Downloader")
win.geometry('500x500')

tkinter.Label(win,text = "URL:").grid(row = 0)
textField = tkinter.Entry(win,width = 60)
textField.grid(row = 0, column = 1)
tkinter.Button(win,text = "Download Audio",command = dAudio).grid(row=3,column=1)
tkinter.Button(win,text = "Download Video",command = dVideo).grid(row=4,column=1)

win.mainloop()
