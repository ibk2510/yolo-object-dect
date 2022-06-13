from deepstack_sdk import ServerConfig, Detection

config = ServerConfig("http://localhost:80")
detection = Detection(config)

detection.detectObjectVideo("v1.mp4",output="video_output.mp4")

print("done processing")