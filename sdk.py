#pip install deepstack-sdk --upgrade

from deepstack_sdk import ServerConfig, Detection

config = ServerConfig("https://yolo-yrh27rcwya-el.a.run.app")
detection = Detection(config)

response = detection.detectObject("./pics/car.jpg")

for obj in response:
   print("Name: {}, Confidence: {}, x_min: {}, y_min: {}, x_max: {}, y_max: {}".format(obj.label, obj.confidence, obj.x_min, obj.y_min, obj.x_max, obj.y_max))