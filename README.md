# basilio-bot

This a Telegram bot to watch my pet dog 'Basilio' (he's a small Jack Russell terrier), with some modifications it can 
watch your pet too.

It works like a state machine with the following states:
- Call: wait to record your voice. 
- PlayCall: play your voice to call your pet.
- WaitHim: Wait for your pet, it just wait until it detects some movement around, using a poor-man motion detection algorithm based on http://www.steinm.com/blog/motion-detection-webcam-python-opencv-differential-images/.
- RecordHim: It will video record your pet.

Combining the states it has the following commands:
- /show: Just show your pet.
- /waitandshow: It will wait until there is some movement and start to record.
- /callandshow: Play your voice and start video recording.
- /callwaitandshow: Like /callandshow but wait for some motion to start recording.

Dependencies:
- python (with cv and telepot)
- vlc (It uses vlc to be able to define the audio device)

