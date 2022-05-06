import subprocess

proc = subprocess.Popen(['sh', '/home/anhduongt/GtkExperiments/ScreenOrientationManager/bin/r.sh', '', 'GXTP7380:00 27C6:0113', ''], stdout=subprocess.PIPE).wait()