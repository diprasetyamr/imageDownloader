**How to run in a container:**
  1. Clone this repository branch docker:
      > git clone -b docker https://github.com/diprasetyamr/imageDownloader.git

      > cd imageDownloader

  2. Build and start the docker container:
      > docker-compose up --build

  3. Open another terminal

  4. Execute the imageDownloader with default urllist file (listUrl.txt):
      > docker-compose exec python python3 imageDownloader

  5. Execute the imageDownloader with custom urllist file:
      > docker-compose exec python python3 imageDownloader filename
