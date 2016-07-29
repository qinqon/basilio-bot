import audioop
import pyaudio

def get_mic_device(paudio, mic_name):
   selected_device = 2
   info = paudio.get_host_api_info_by_index(0)
   numdevices = info.get('deviceCount')
#for each audio device, determine if is an input or an output and add it to the appropriate list and dictionary
   for i in range (0,numdevices):
      if paudio.get_device_info_by_host_api_device_index(0,i).get('maxInputChannels')>0:
         device_name = paudio.get_device_info_by_host_api_device_index(0,i).get('name')
         if device_name.find(mic_name) > -1: 
            selected_device = i
            break

   device_info = paudio.get_device_info_by_index(selected_device)
   print "Selected device is ",device_info.get('name')
   return selected_device
#

def get_level(data):
   rms = audioop.rms(data, 2)  #width=2 for format=paInt16
   return rms


def wait_for_cry(threshold):
   p = pyaudio.PyAudio()
   mic_device = get_mic_device(p, "USB")
   chunk = 1024

   stream = p.open(format=pyaudio.paInt16,
                   input_device_index=mic_device,
                   channels=1,
                   rate=48000,
                   input=True,
                   output=False,
                   frames_per_buffer=chunk)

   # wait until the sound data breaks some level threshold
   while True:
      try:
         data = stream.read(chunk)
         if get_level(data) > threshold:
            break
      except IOError:
         print "Ignoring chunk"
   
   p.terminate()

wait_for_cry(threshold=20000)
