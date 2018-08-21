import urllib.request
import os

def downloadImageFromFile(urlfile):
    saveFolder = 'images'
    if not os.path.exists(saveFolder):
        os.makedirs(saveFolder)

    with open(urlfile, encoding='utf-8') as f:
        for lines in f.readlines():
            # Remove \n from the string
            url = lines[:len(lines)-1:]

            # Splitting the URL path to be used later on for determining the name of the file from the URL
            filename = url.split("/")

            print("Downloading from:", url)
            print("Status:", download_file(url, os.path.join(saveFolder, filename[len(filename) - 1])))

def download_file(url, filename):
    try:
        # Fix for HTTP 403 Forbidden
        req = urllib.request.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })

        res = urllib.request.urlopen(req)
        meta = res.info()

        # Download only image file
        if (meta["Content-Type"]).split("/")[0] == "image":
            if meta["Content-Length"] is not None:
                filesize = int(meta["Content-Length"])
                print("File Size: %.2f kb"%(filesize/1024))
            with open(filename, 'wb') as f:
                while True:
                    buffer = res.read(1024)
                    if not buffer: break
                    f.write(buffer)
            res.close()
            return "Image Downloaded"
        else:
            res.close()
            return "Image Not Found"
    except Exception as e:
        return e.reason
