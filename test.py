# Port of
# http://git.kernel.org/?p=linux/hotplug/udev.git;a=blob;f=extras/gudev/gjs-example.js

import sys
sys.path.insert(0, ".libs")

import gudev
import glib

def print_device(device):
    print "subsystem", device.get_subsystem ()
    print "devtype", device.get_devtype ()
    print "name", device.get_name ()
    print "number", device.get_number ()
    print "sysfs_path:", device.get_sysfs_path ()
    print "driver:", device.get_driver ()
    print "action:", device.get_action ()
    print "seqnum:", device.get_seqnum ()
    print "device type:", device.get_device_type ()
#    print "device number:", device.get_device_number ()
    print "device file:", device.get_device_file ()

def on_uevent(client, action, device):
    print "UEVENT"
    print_device(device)

client = gudev.Client(["block","usb/usb_interface"])
client.connect("uevent", on_uevent)

devices = client.query_by_subsystem("block")
for device in devices:
    print_device(device)

glib.MainLoop().run()
