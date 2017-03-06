import sys

try:
	import numpy as np
except ImportError:
	print 'could not import numpy, aborting...'
	sys.exit(-1)

#consider adding bipolar argument

class Parameter(object):
	def __init__(self,name,nrpn_a,nrpn_b,low,high,init=None,cc_id=None):
		self.name = name
		self.nrpn_a = nrpn_a
		self.nrpn_b = nrpn_b
		self.low = low
		self.high = high
		if init is not None:
			if init < low or init > high:
				self.val = low
			else:
				self.val = init
		if cc_id is not None:
			self.cc_id = cc_id

	def make_nrpn_msg(self,channel,val=None,layer='a'):
		header_byte = 0xb0 | channel
		v = self.val if (val is None) else val
		l = self.nrpn_a if layer == 'a'else self.nrpn_b
		bints = [[header_byte, 0x63, 0x7f & (l >> 8)],
					[header_byte, 0x62, 0x7f & l],
					[header_byte, 0x06, 0x7f & (v >> 8)],
					[header_byte, 0x26, 0x7f & v],
					[header_byte, 0x60, 0],
					[header_byte, 0x61, 0],
					[header_byte, 0x25, 0x7f],
					[header_byte, 0x24, 0x7f]]
		return bints

	def make_nrpn_runiform_msg(self,channel,rlow,rhigh):
		r = int(np.round(np.random.uniform(rlow,rhigh)))
		if r > self.high:
			r = self.high
		elif r < self.low:
			r = self.low
		return self.make_nrpn_msg(channel,val=r)

	def make_nrpn_rgauss_msg(self,channel,mean,sigma):
		r = int(np.round(np.random.normal(loc=mean,scale=sigma)))
		if r > self.high:
			r = self.high
		elif r < self.low:
			r = self.low
		return self.make_nrpn_msg(channel,val=r)

ParameterList = [
	Parameter('osc1pitch',0,512,0,120),
	Parameter('osc1finetune',1,513,0,100),
	Parameter('osc1level',2,514,0,127),
	Parameter('osc1shape',3,515,0,19),
	Parameter('osc1shapemod',4,516,0,127),
	Parameter('osc1waveleft',5,517,0,11),
	Parameter('osc1waveright',6,518,0,11),
	Parameter('osc1fm',7,519,0,255),
	Parameter('osc1am',8,520,0,255),
	Parameter('osc1slop',9,521,0,127),
	Parameter('osc1glideamount',10,522,0,127),
	Parameter('osc1sync',11,523,0,1),
	Parameter('osc1keyfollow',12,524,0,1),
	Parameter('osc1wavereset',13,525,0,1),
	Parameter('osc2pitch',18,530,0,120),
	Parameter('osc2finetune',19,531,0,100),
	Parameter('osc2level',20,532,0,127),
	Parameter('osc2shape',21,533,0,19),
	Parameter('osc2shapemod',22,534,0,127),
	Parameter('osc2waveleft',23,535,0,11),
	Parameter('osc2waveright',24,536,0,11),
	Parameter('osc2fm',25,537,0,255),
	Parameter('osc2am',26,538,0,255),
	Parameter('osc2slop',27,539,0,127),
	Parameter('osc2glideamount',28,540,0,127),
	Parameter('osc2sync',29,541,0,1),
	Parameter('osc2keyfollow',30,542,0,1),
	Parameter('osc2wavereset',31,543,0,1),
	Parameter('osc3pitch',36,548,0,120),
	Parameter('osc3finetune',37,549,0,100),
	Parameter('osc3level',38,550,0,127),
	Parameter('osc3shape',39,551,0,19),
	Parameter('osc3shapemod',40,552,0,127),
	Parameter('osc3waveleft',41,553,0,11),
	Parameter('osc3waveright',42,554,0,11),
	Parameter('osc3fm',43,555,0,255),
	Parameter('osc3am',44,556,0,255),
	Parameter('osc3slop',45,557,0,127),
	Parameter('osc3glideamount',46,558,0,127),
	Parameter('osc3sync',47,559,0,1),
	Parameter('osc3keyfollow',48,560,0,1),
	Parameter('osc3wavereset',49,561,0,1),
	Parameter('osc4pitch',54,566,0,120),
	Parameter('osc4finetune',55,567,0,100),
	Parameter('osc4level',56,568,0,127),
	Parameter('osc4shape',57,569,0,19),
	Parameter('osc4shapemod',58,570,0,127),
	Parameter('osc4waveleft',59,571,0,11),
	Parameter('osc4waveright',60,572,0,11),
	Parameter('osc4fm',61,573,0,255),
	Parameter('osc4am',62,574,0,255),
	Parameter('osc4slop',63,575,0,127),
	Parameter('osc4glideamount',64,576,0,127),
	Parameter('osc4sync',65,577,0,1),
	Parameter('osc4keyfollow',66,578,0,1),
	Parameter('osc4wavereset',67,579,0,1),
	Parameter('osc1suboctave',72,584,0,127),
	Parameter('glidemode',73,585,0,3),
	Parameter('glide',74,586,0,1),
	Parameter('pitchbendrangeup',75,587,0,12),
	Parameter('pitchbendrangedown',76,588,0,24),
	Parameter('air',80,592,0,127),
	Parameter('girth',81,593,0,127),
	Parameter('hack',82,594,0,127),
	Parameter('decimate',83,595,0,127),
	Parameter('drive',84,596,0,127),
	Parameter('lpffrequency',90,602,0,164),
	Parameter('lpfresonance',91,603,0,127),
	Parameter('lpfkeyamount',92,604,0,127),
	Parameter('lpf24pole',93,605,0,1),
	Parameter('hpffrequency',94,606,0,127),
	Parameter('hpfresonance',95,607,0,127),
	Parameter('hpfkeyamount',96,608,0,127),
	Parameter('feedbackamount',97,609,0,254),
	Parameter('feedbacktuning',98,610,0,48),
	Parameter('voicevolume',99,611,0,127),
	Parameter('panspread',100,612,0,127),
	Parameter('distortionamount',101,613,0,127),
	Parameter('vcaenvelopeamount',103,615,0,127),
	Parameter('velocitytovcaenvamount',104,616,0,127),
	Parameter('vcaenvdelay',105,617,0,127),
	Parameter('vcaenvattack',106,618,0,127),
	Parameter('vcaenvdecay',107,619,0,127),
	Parameter('vcaenvsustain',108,620,0,127),
	Parameter('vcaenvrelease',109,621,0,127),
	Parameter('vcaenvrepeat',110,622,0,1),
	Parameter('lpfenvelopeamount',114,626,0,254),
	Parameter('veloctytolpfenvamount',115,627,0,127),
	Parameter('lpfenvdelay',116,628,0,127),
	Parameter('lpfenvattack',117,629,0,127),
	Parameter('lpfenvdecay',118,630,0,127),
	Parameter('lpfenvsustain',119,631,0,127),
	Parameter('lpfenvrelease',120,632,0,127),
	Parameter('lpfenvrepeat',121,633,0,1),
	Parameter('envelope3amt',125,637,0,254),
]

ParameterDict = {p.name:p for p in ParameterList}
