# test_audio.py
# A temporary utility to list all available audio devices and their indices.
import pyaudio

p = pyaudio.PyAudio()

print("--- Searching for Audio Devices ---\n")

try:
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')

    print("Found a total of {} audio devices.\n".format(numdevices))

    for i in range(0, numdevices):
        device_info = p.get_device_info_by_host_api_device_index(0, i)
        
        print(f"Device Index: {device_info.get('index')}")
        print(f"  Name: {device_info.get('name')}")
        print(f"  Input Channels: {device_info.get('maxInputChannels')}")
        print(f"  Output Channels: {device_info.get('maxOutputChannels')}")
        print("-" * 25)

except Exception as e:
    print(f"Could not get device info: {e}")

finally:
    p.terminate()