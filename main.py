#import mido
import math
import socket
import time
import os

os.system('title among us')

ip=input('192.168.')
ip='192.168.'+ip
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,7331))
s.send(bytes.fromhex('03'))
s.send(bytes.fromhex('10014CFC00000000'))
tmp='C0000010600000009421FFE07C0802A6900100243C60109D8063D8E4806300342C030000418200483D801002804C1E502C02000041820038818C1E543C80109C808465A091810040C0210040C04100403D80031E618CA16C7D8903A64E800421384000003D801002904C1E50800100247C0803A6382100203D80010F618C6AE07D8903A64E800420'
for x in range(math.floor(len(tmp)/8)):
    s.send(bytes.fromhex('03'))
    s.send(bytes.fromhex('0'+format(0x01133000+x*4,'X')+tmp[x*8:x*8+8]))
s.send(bytes.fromhex('03'))
s.send(bytes.fromhex('10014CFC00000001'))
#mid = mido.MidiFile('a.mid')

#for msg in mid.tracks[0]:
#    if msg.type == 'note_on':
#        text=str(msg)
#        text=text.replace('note_on channel=0 ','')
#        pich=int(text[text.index('note=')+5:text.index(' ')])
#        times=int(text[text.index('time=')+5:])
s.send(bytes.fromhex('03'))
s.send(bytes.fromhex('10021E54C1000000'))
s.send(bytes.fromhex('03'))
s.send(bytes.fromhex('10021E5000000001'))
time.sleep(0.7)
s.send(bytes.fromhex('03'))
s.send(bytes.fromhex('10021E5441380000'))
s.send(bytes.fromhex('03'))
s.send(bytes.fromhex('10021E5000000001'))
time.sleep(0.45)
s.send(bytes.fromhex('03'))
s.send(bytes.fromhex('10021E5441580000'))
s.send(bytes.fromhex('03'))
s.send(bytes.fromhex('10021E5000000001'))
time.sleep(0.45)
s.send(bytes.fromhex('03'))
s.send(bytes.fromhex('10021E5441700000'))
s.send(bytes.fromhex('03'))
s.send(bytes.fromhex('10021E5000000001'))
time.sleep(0.63)
s.send(bytes.fromhex('03'))
s.send(bytes.fromhex('10021E5441800000'))
s.send(bytes.fromhex('03'))
s.send(bytes.fromhex('10021E5000000001'))
s.close()
