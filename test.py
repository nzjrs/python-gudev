import sys
sys.path.insert(0, ".libs")

import gudev

c = gudev.Client("block")
devices = c.query_by_subsystem('block')
for device in devices:
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
#    print "device file symlinks:", device.get_device_file_symlinks ()
