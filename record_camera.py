import ffmpeg
from datetime import datetime
from dotenv import load_dotenv
import os
from get_filesize import file_size

load_dotenv()

camera_ip = os.getenv("CAMERA_IP")
camera_port = os.getenv("CAMERA_PORT")
camera_user = os.getenv("CAMERA_USER")
camera_password = os.getenv("CAMERA_PASSWORD")



rtsp_url = f"rtsp://{camera_user}:{camera_password}@{camera_ip}:{camera_port}/onvif2"

filename = f"./records/recording_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"

try:
    (
        ffmpeg
        .input(rtsp_url, rtsp_transport='udp', t=60)
        .output(filename, r=8)  # Cambiar FPS a 8
        .run()
    )
    print(f"Grabación completada: {filename}")
    print("filesize:", file_size(filename))
except ffmpeg.Error as e:
    print(f"Error de FFmpeg: {e}")

