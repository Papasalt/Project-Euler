import tkinter as tk
import tkinter.filedialog
import yt_dlp as ytdl
import tempfile
import PIL
from PIL import Image, ImageTk
import glob

factor = 12
size = (16*factor, 9*factor)

class App:
    def __init__(self):
        self.temp = tempfile.TemporaryDirectory()
        self.temp_path = self.temp.name.replace("\\","/")
        self.tempThumbnailPath = self.temp_path + "/thumbnail.%(ext)s"
        
        thumbnail_ydl = {"outtmpl":self.tempThumbnailPath,
              "writethumbnail":True,
              "skip_download":True}
        
        self.ydl = ytdl.YoutubeDL(thumbnail_ydl)
        
        self.window = tk.Tk()
        self.thumbnailFrame = tk.Frame()
        self.thumbnailFrame.pack()
        
        self.thumbnailPath = r"C:\Users\papas\Downloads\Visual YTDL\thumbnailHold.png"
        self.thumbnail = PIL.Image.open(self.thumbnailPath)
        self.thumbnail = self.thumbnail.resize(size)
        self.thumbnailImage = PIL.ImageTk.PhotoImage(self.thumbnail)
        self.thumbnailLabel = tk.Label(master=self.thumbnailFrame, image=self.thumbnailImage)
        
        self.savePath = tk.StringVar()
        self.updatePath = tk.Button(self.window, text="Select Folder...", command=lambda: self.updateSavePath())
        self.printPath = tk.Button(self.window, text="Print", command=lambda: self.printSavePath())
        self.getImage = tk.Button(self.window, text="Get Image", command=lambda: self.getThumbnail())
        self.youtubeEntry = tk.Entry(self.window, width=75)
        
        self.pathLabel = tk.Label(self.window, relief="sunken", textvariable=self.savePath, width=100)
        
        self.thumbnailLabel.pack()
        self.updatePath.pack()
        self.pathLabel.pack()
        self.printPath.pack()
        self.getImage.pack()
        self.youtubeEntry.pack()
        
        self.window.title("Visual YTDL")
        self.window.geometry("800x600")
        self.window.mainloop()
    
    def updateSavePath(self):
        self.savePath.set(tk.filedialog.askdirectory())
    
    def printSavePath(self):
        print(self.savePath.get())
    
    def getThumbnail(self):
        print(self.thumbnailPath)
        self.downloadTempThumbnail()
        
        self.thumbnail = PIL.Image.open(self.thumbnailPath)
        self.thumbnail = self.thumbnail.resize(size)
        self.thumbnailImage = PIL.ImageTk.PhotoImage(self.thumbnail)
        self.thumbnailLabel.configure(image=self.thumbnailImage)
        self.thumbnailLabel.image=self.thumbnailImage
        print(self.thumbnailPath)
    
    def downloadTempThumbnail(self):
        try:
            self.ydl.download([self.youtubeEntry.get()])
            self.thumbnailPath = glob.glob(self.temp_path + "/thumbnail.*")[0]
        except:
            self.thumbnailPath =self.thumbnailPath
            print("Unexpected URL")

Window = App()
"""
ydl_format = {"outtmpl":r"C:/Users/papas/Downloads/Visual YTDL/%(title)s.%(ext)s",
              "writethumbnail":True,
              "skip_download":True}

ydl = ytdl.YoutubeDL(ydl_format)
ydl.download(["https://www.youtube.com/watch?v=s1MGTENLNLw"])"""