from pytube import YouTube

link = input("Enter the YouTube video URL: ")

def Download(link):
    yt = YouTube(link)
    try:
        youtubeObject = yt.streams.get_highest_resolution().download()
        print("Download is completed successfully")
    except:
        print("An error has occurred")
    

Download(link)



