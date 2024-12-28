#!/bin/python3
import dbus
import dbus.bus
import wx
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

import threading
import config_utils
import ffmpeg_utils

config = config_utils.load_config()

video_directory = config["directory"]


print("Initial video directory: " + video_directory)


old_text: str = ""
status_button: wx.Button = None


def done_extracting(video_directory: str):
    global status_button, old_text
    status_button.SetLabelText(old_text)

    bus = dbus.SessionBus()
    proxy = bus.get_object('org.freedesktop.FileManager1', '/org/freedesktop/FileManager1')
    interface = dbus.Interface(proxy, dbus_interface='org.freedesktop.FileManager1')
    interface.ShowFolders(["file://" + video_directory], "")


def extract_in_background(filename, output_directory):
    ffmpeg_utils.extract_tracks_from_video(filename, output_directory)
    wx.CallAfter(lambda: done_extracting(output_directory))


class DropTarget(wx.FileDropTarget):
    def __init__(self, obj):
        wx.FileDropTarget.__init__(self)
        self.obj = obj

    def OnDropFiles(self, x, y, filenames):
        global video_directory

        print("Drop Event", filenames)

        for filename in filenames:
            status_button.SetLabelText("Processing...")
            threading.Thread(target=extract_in_background, args=(filename, video_directory)).start()

        return True


class MyFrame(wx.Frame):

    def __init__(self, parent, ID, title):
        global status_button, old_text

        wx.Frame.__init__(self, parent, ID, title, size=(400,500))

        self.SetMinSize((400,500))
        self.SetMaxSize((400,500))

        panel1 = wx.Panel(self, -1, style=wx.SUNKEN_BORDER)
        panel2 = wx.Panel(self, -1, style=wx.SUNKEN_BORDER)

        old_text = 'Drag a file over'

        status_button = wx.Button(panel2, -1, label=old_text, size=(400,500))
        status_button.Bind(wx.EVT_BUTTON, self.on_button)

        pro_tip = wx.StaticText(self, 2, label='or press here to change the target directory')
        pro_tip.SetForegroundColour((150,150,150))
        pro_tip.SetPosition((70, 270))

        self.file_drop_target = DropTarget(self)
        self.SetDropTarget(self.file_drop_target)

        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(panel1, 0, wx.EXPAND,0)
        box.Add(panel2, 0, wx.EXPAND,0)

        self.SetAutoLayout(True)
        self.SetSizer(box)
        self.Layout()
    
    def on_button(self, event):
        global video_directory

        tmp_dir = wx.DirSelector()
        
        if tmp_dir == "":
            print("No directory selected")
            return
        
        video_directory = tmp_dir
        print("New directory selected:", video_directory)

        config["directory"] = video_directory
        config_utils.save_config(config)
 
    def OnClose(self, e):
        self.Close(True)


app = wx.App()
frame = MyFrame(None, -1, "Get Rid of AAC")
frame.Show()
app.MainLoop()
