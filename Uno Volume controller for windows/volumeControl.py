import os
import serial

# Dependencies:
# https://github.com/pyserial/pyserial


# Python listens on a port
ser = serial.Serial('COM3', 9600)
volume = ""
while True:
	# read in the value from arduino
	response = ser.readline().decode("utf-8",errors="ignore").strip()
	# make sure the value isn't null
	if(response):
		# if the response is different
		if(volume != response):
			volume = response
			print(volume +'0%')
			if(volume == '0'):
				# call NirCmd (windows script) to change the volume
				command = 'NirCmd.exe setsysvolume 0'
				os.system(command)
			elif(volume == '8'):
				# call NirCmd (windows script) to change the volume
				command = 'NirCmd.exe setsysvolume 65535'
				os.system(command)
			elif(volume == '7'):
				# call NirCmd (windows script) to change the volume
				command = 'NirCmd.exe setsysvolume 57343'
				os.system(command)
			elif(volume == '6'):
				# call NirCmd (windows script) to change the volume
				command = 'NirCmd.exe setsysvolume 49151'
				os.system(command)
			elif(volume == '5'):
				# call NirCmd (windows script) to change the volume
				command = 'NirCmd.exe setsysvolume 40959'
				os.system(command)
			elif(volume == '4'):
				# call NirCmd (windows script) to change the volume
				command = 'NirCmd.exe setsysvolume 32767'
				os.system(command)
			elif(volume == '3'):
				# call NirCmd (windows script) to change the volume
				command = 'NirCmd.exe setsysvolume 24575'
				os.system(command)
			elif(volume == '2'):
				# call NirCmd (windows script) to change the volume
				command = 'NirCmd.exe setsysvolume 16383'
				os.system(command)
			elif(volume == '1'):
				# call NirCmd (windows script) to change the volume
				command = 'NirCmd.exe setsysvolume 8192'
				os.system(command)
			else:
				# call NirCmd (windows script) to change the volume
				command = 'NirCmd.exe setsysvolume 0'
				os.system(command)