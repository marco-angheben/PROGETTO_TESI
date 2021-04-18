#

## How to run it

To run the frontend (Linux Ubuntu required):

* Install python 3 on your machine
* Clone this repo 
* Open the root folder in a terminal
* Execute `pip3 install -r requirements.txt` to install the python dependencies
* Execute `apt install libsm6 libxrender1 libfontconfig1 libice6` to install some needed apt dependencies for opencv
* Download from here [https://pjreddie.com/media/files/yolov3.weights](https://pjreddie.com/media/files/yolov3.weights) the yolov3 weights and put them in `/analyzer/weights/yolov3.weights`
* Execute `./run.sh` to start the server
* You can now make requests on the address 'http://localhost:5000'

The server is very very slow to process the video. If you need a bigger timeout, change the file `run.sh`, set the timeout in seconds after `--timeout`

