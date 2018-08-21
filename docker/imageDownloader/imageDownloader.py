import urllib.request

def downloadImageFromFile(urlfile):
    with open(urlfile, encoding='utf-8') as f:
        for lines in f.readlines():
            # Remove \n from the string
            url = lines[:len(lines)-1:]

            # Splitting the URL path to be used later on for determining the name of the file from the URL
            filename = url.split("/")

            print("Downloading from:", url)
            print("Status:", download_file(lines, filename[len(filename) - 1]))

def download_file(url, filename):
    try:
        # Add header to the request, to fix 403 Forbidden problem
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
        return "Image Not Found"
