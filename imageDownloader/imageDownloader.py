import urllib.request
import os

def check_url(url):
    try:
        # Try to build request
        req = urllib.request.Request(
            url, headers={'User-Agent': 'Mozilla/5.0'})

        return True
    except Exception as e:
        return False

def downloadImageFromFile(urlfile):
    saveFolder = 'images'

    # Create folder if does not exist
    if not os.path.exists(saveFolder):
        os.makedirs(saveFolder)

    with open(urlfile, encoding='utf-8') as f:
        for lines in f.readlines():

            # Remove \n from the string
            url = lines[:len(lines) - 1:]

            # Splitting the URL path to be used later on for
            # determining the name of the file from the URL
            filename = url.split("/")

            print("Downloading from:", url)
            print("Status:", download_file(url, os.path.join(
                saveFolder, filename[len(filename) - 1])))

def download_file(url, filename):
    # Check URL
    if check_url(url):
        req = urllib.request.Request(
            url, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            # Try to send the request and get the respond
            res = urllib.request.urlopen(req)

            # Get the metadata from the respond
            meta = res.info()

            # Download image file only
            if (meta["Content-Type"]).split("/")[0] == "image":

                # Check if there is a pre-defined
                # Content Size inside the metadata
                if meta["Content-Length"] is not None:
                    filesize = int(meta["Content-Length"])
                    print("File Size: %.2f kb" % (filesize / 1024))
                else:
                    print("File Size: Unknown")

                # Write to file
                with open(filename, 'wb') as f:
                    while True:
                        buffer = res.read(1024)
                        if not buffer:
                            break
                        f.write(buffer)

                res.close()
                return "Image Downloaded"
            else:
                res.close()
                return "Image Not Found"
        except Exception as e:
            return e
    else:
        return "URL unknown"
