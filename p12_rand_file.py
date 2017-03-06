from pygame import midi
from sys import exit
from argparse import ArgumentParser
from P12Randomizer import ParameterDict
p = ArgumentParser(description='randomize prophet 12 parameters from a file')
p.add_argument('file',help='file containing randomization specification')
p.add_argument('--midi_info',action='store_true',help='list the midi info, then exit')
p.add_argument('--channel',type=int,help='midi channel to send on',default=0)
p.add_argument('--device_id',type=int,help='integer device id, get device info by using option --midi_info.  if this option is not specified, the default as  returned by pygame.midi will be used')
a = p.parse_args()
midi.init()

if a.midi_info:
	for i in xrange(midi.get_count()):
		print midi.get_device_info(i)
	exit(0)

a.channel -= 1
if a.channel < 0 or a.channel > 15:
	print 'bad channel number, must be 1-16...'
	exit(-1)

if a.device_id is None:
	d = midi.get_default_output_id()
	print 'using default device: ',d
else:
	try:
		if midi.get_device_info(a.device_id)[3] == 1:
			d = a.device_id
			print 'using user specified device id = ',d
		else:
			d = midi.get_default_output_id()
			print 'user specified id is not an output, using default id = ',d
	except:
		d = midi.get_default_output_id()
		print 'error using user specified id... using default id = ',d
		
try:
	m = midi.Output(d)
except Exception as e:
	print 'exception when opening midi device: ',e
	exit(-1)

try:
	f = open(a.file)
except Exception as e:
	print 'exception when opening file: ',e
	m.close()
	exit(-1)

pt = [l.split() for l in f]

while 1:
	inp = raw_input('>>> ')
	if inp == 'q':
		m.close()
		exit(0)
	elif inp == 'r':
		for x in pt:
			if ParameterDict.has_key(x[0]):
				if x[1] == 'u':
					#uniform
					messages = ParameterDict[x[0]].make_nrpn_runiform_msg(a.channel,int(x[2]),int(x[3]))
					m.write(zip(messages,[midi.time() for i in range(len(messages))]))
				elif x[1] == 'g':
					messages = ParameterDict[x[0]].make_nrpn_rgauss_msg(a.channel,int(x[2]),int(x[3]))
					m.write(zip(messages,[midi.time() for i in range(len(messages))]))
					#gauss
				else:
					print 'bad entry in file: ',x,', need either \'u\' or \'g\' as as second field'
			else:
				print 'bad entry in file: ',x,', parameter does not exist'
	else:
		print 'enter \'r\' to randomize or \'q\' to quit'
