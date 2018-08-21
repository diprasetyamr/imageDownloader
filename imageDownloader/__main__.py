from imageDownloader import downloadImageFromFile
import sys

if __name__ == '__main__':
    # If there is an argument input for
    # taking a different urllist file
    if len(sys.argv) > 1:
        downloadImageFromFile(sys.argv[1])
    else:
        downloadImageFromFile('listUrl.txt')
