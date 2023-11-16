Steel eagle:
cd ~/openscout/server
git checkout steel-eagle
docker build -t cmusatylab/openscout:steel-eagle .
cd ~/steel-eagle/cnc/server
vim .env
<copy following stuff into .env>
cp ~/openscout/server/models/coco.pt ~/steel-eagle/cnc/server/models
cd ~/steel-eagle/cnc/server
git pull
docker build -t cmusatyalab/steel-eagle:latest .
docker-compose up




following stuff:
#Steel-Eagle variables
#Drones are invalidated if we don't hear from them for this many seconds
DRONE_TIMEOUT=120
TAG=latest
#OpenScout variables
OPENSCOUT_TAG=steel-eagle
#ELK OSS version
#ELK_VERSION=7.10.2
ELK_VERSION=7.9.3
#optionally store images with bounding boxes STORE=--store
STORE=--store
#leave STORE unassigned otherwise
#STORE=
FAUX=
HTTP_PORT=8080
WEBSERVER_URL=http://cloudlet033.elijah.cs.cmu.edu
#face-engine
FACE_THRESHOLD=0.5
#object-engine
DNN=coco
OBJ_THRESHOLD=0.5
EXCLUSIONS=
#obstacle avoidance
MIDAS=DPT_Large
DEPTH_THRESHOLD=150

