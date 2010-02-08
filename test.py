# Port of
# http://git.kernel.org/?p=linux/hotplug/udev.git;a=blob;f=extras/gudev/gjs-example.js

import sys
sys.path.insert(0, ".libs")

import gudev
import glib

print "GUDEV VERSION: %s" % gudev.__version__

def print_device(device):
    print "subsystem", device.get_subsystem()
    print "devtype", device.get_devtype()
    print "name", device.get_name()
    print "number", device.get_number()
    print "sysfs_path:", device.get_sysfs_path()
    print "driver:", device.get_driver()
    print "action:", device.get_action()
    print "seqnum:", device.get_seqnum()
    print "device type:", device.get_device_type()
    print "device number:", device.get_device_number()
    print "device file:", device.get_device_file()
    print "device file symlinks:", ", ".join(device.get_device_file_symlinks())
    print "device keys:", ", ".join(device.get_property_keys())

def on_uevent(client, action, device):
    print "UEVENT"
    print_device(device)
    print "------", device.get_property("ID_MEDIA_PLAYER")

client = gudev.Client(["block","usb"])
client.connect("uevent", on_uevent)

devices = client.query_by_subsystem("usb")
for device in devices:
    print_device(device)

glib.MainLoop().run()
