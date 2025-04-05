from dotenv import load_dotenv
import os
from roboflow import Roboflow

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from environment variables
api_key = os.getenv('ROBOFLOW_API_KEY')

rf = Roboflow(api_key=api_key)
project = rf.workspace("traintrackproject").project("traintracks")
dataset = project.version(4).download("yolov5")
