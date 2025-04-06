from roboflow import Roboflow
rf = Roboflow(api_key="oZltBsIelh6plGNiCtH5")
project = rf.workspace("y0").project("railway-tracks-tpu61-mv0ja")
version = project.version(1)
dataset = version.download("yolov8")