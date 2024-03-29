from app import App
import tkinter as tk
import json
import os

def main():
    # print(sys.argv)
    # print(type(sys.argv[1]))

    try:
        f=open("settings.json","r")
        settings=json.load(f)
        print(f"Settings file found here: {os.path.realpath(f.name)}")
        print(settings)
        f.close()
    except:
        settings = {
            "video_source" : 0,
            # "video_source" : "video_samples/4.mp4",
            "show_video" : True,
            "auto_detect_orientation" : True,
            "draw_all_landmarks" : False,
            "draw_pose_landmarks" : True,
            "vis_threshold" : 0.7,
            "neck_ratio_threshold" : 0.65,
            "neck_angle_threshold" : 60,
            "shoulder_height_variation_threshold" : 0.018,
            "shoulder_hip_ratio_threshold" : 0.45,
            "put_orientation_text" : True,
            "resize_image_width_to" : 400,
            "resize_image_height_to" : None,
            "time_bad_posture_alert" : 3,
            "show_fps" : False,
            "mirror_mode" : True,
            "alert_other_device": False,
            "alert_sound": False,
            "ip_address": None,
        }

        with open('settings.json', 'w') as f:
            json.dump(settings, f, indent=2, separators=(", ", ": "))
        print(f"settings file not found, created on with default settings here: {os.path.realpath(f.name)}")

    App(tk.Tk(), "Tkinter and OpenCV", **settings)
    

if __name__ == "__main__":
    main()