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
	Parameter('velocitytoenv3amt',126,638,0,127)
	Parameter('envelope3delay',127,639,0,127)
	Parameter('envelope3attack',128,640,0,127)
	Parameter('envelope3decay',129,641,0,127)
	Parameter('envelope3sustain',130,642,0,127)
	Parameter('envelope3release',131,643,0,127)
	Parameter('envelope3repeat',132,644,0,1)
	Parameter('envelope3destination',133,645,0,97)
	Parameter('envelope4amt',136,648,0,254)
	Parameter('velocitytoenv4amt',137,649,0,127)
	Parameter('envelope4delay',138,650,0,127)
	Parameter('envelope4attack',139,651,0,127)
	Parameter('envelope4decay',140,652,0,127)
	Parameter('envelope4sustain',141,653,0,127)
	Parameter('envelope4release',142,654,0,127)
	Parameter('envelope4repeat',143,655,0,1)
	Parameter('envelope4destination',144,656,0,97)
	Parameter('lfo1frequency',147,659,0,255)
	Parameter('lfo1syncsetting',148,660,0,15)
	Parameter('lfo1sync',149,661,0,1)
	Parameter('lfo1shape',150,662,0,7)
	Parameter('lfo1amount',151,663,0,127)
	Parameter('lfo1slewrate',152,664,0,127)
	Parameter('lfo1phase',153,665,0,127)
	Parameter('lfo1wavereset',154,666,0,1)
	Parameter('lfo1destination',155,667,0,97)
	Parameter('lfo2frequency',157,669,0,255)
	Parameter('lfo2syncsetting',158,670,0,15)
	Parameter('lfo2sync',159,671,0,1)
	Parameter('lfo2shape',160,672,0,7)
	Parameter('lfo2amount',161,673,0,127)
	Parameter('lfo2slewrate',162,674,0,127)
	Parameter('lfo2phase',163,675,0,127)
	Parameter('lfo2wavereset',164,676,0,1)
	Parameter('lfo2destination',165,677,0,97)
	Parameter('lfo3frequency',167,679,0,255)
	Parameter('lfo3syncsetting',168,680,0,15)
	Parameter('lfo3sync',169,681,0,1)
	Parameter('lfo3shape',170,682,0,7)
	Parameter('lfo3amount',171,683,0,127)
	Parameter('lfo3slewrate',172,684,0,127)
	Parameter('lfo3phase',173,685,0,127)
	Parameter('lfo3wavereset',174,686,0,1)
	Parameter('lfo3destination',175,687,0,97)
	Parameter('lfo4frequency',177,689,0,255)
	Parameter('lfo4syncsetting',178,690,0,15)
	Parameter('lfo4sync',179,691,0,1)
	Parameter('lfo4shape',180,692,0,7)
	Parameter('lfo4amount',181,693,0,127)
	Parameter('lfo4slewrate',182,694,0,127)
	Parameter('lfo4phase',183,695,0,127)
	Parameter('lfo4wavereset',184,696,0,1)
	Parameter('lfo4destination',185,697,0,97)
	Parameter('delay1time',187,699,0,255)
	Parameter('delay1syncsetting',188,700,0,11)
	Parameter('delay1sync',189,701,0,1)
	Parameter('delay1amount',190,702,0,127)
	Parameter('delay1feedback',191,703,0,127)
	Parameter('delay1lowpassfilter',192,704,0,127)
	Parameter('delay1highpassfilter',193,705,0,127)
	Parameter('delay1filtermode',194,706,0,1)
	Parameter('delay2time',195,707,0,255)
	Parameter('delay2syncsetting',196,708,0,11)
	Parameter('delay2sync',197,709,0,1)
	Parameter('delay2amount',198,710,0,127)
	Parameter('delay2feedback',199,711,0,127)
	Parameter('delay2lowpassfilter',200,712,0,127)
	Parameter('delay2highpassfilter',201,713,0,127)
	Parameter('delay2filtermode',202,714,0,1)
	Parameter('delay3time',203,715,0,255)
	Parameter('delay3syncsetting',204,716,0,11)
	Parameter('delay3sync',205,717,0,1)
	Parameter('delay3amount',206,718,0,127)
	Parameter('delay3feedback',207,719,0,127)
	Parameter('delay3lowpassfilter',208,720,0,127)
	Parameter('delay3highpassfilter',209,721,0,127)
	Parameter('delay3filtermode',210,722,0,1)
	Parameter('delay4time',211,723,0,255)
	Parameter('delay4syncsetting',212,724,0,11)
	Parameter('delay4sync',213,725,0,1)
	Parameter('delay4amount',214,726,0,127)
	Parameter('delay4feedback',215,727,0,127)
	Parameter('delay4lowpassfilter',216,728,0,127)
	Parameter('delay4highpassfilter',217,729,0,127)
	Parameter('delay4filtermode',218,730,0,1)
	Parameter('mod1source',219,731,0,26)
	Parameter('mod1amount',220,732,0,254)
	Parameter('mod1destination',221,733,0,97)
	Parameter('mod2source',223,735,0,26)
	Parameter('mod2amount',224,736,0,254)
	Parameter('mod2destination',225,737,0,97)
	Parameter('mod3source',227,739,0,26)
	Parameter('mod3amount',228,740,0,254)
	Parameter('mod3destination',229,741,0,97)
	Parameter('mod4source',231,743,0,26)
	Parameter('mod4amount',232,744,0,254)
	Parameter('mod4destination',233,745,0,97)
	Parameter('mod5source',235,747,0,26)
	Parameter('mod5amount',236,748,0,254)
	Parameter('mod5destination',237,749,0,97)
	Parameter('mod6source',239,751,0,26)
	Parameter('mod6amount',240,752,0,254)
	Parameter('mod6destination',241,753,0,97)
	Parameter('mod7source',243,755,0,26)
	Parameter('mod7amount',244,756,0,254)
	Parameter('mod7destination',245,757,0,97)
	Parameter('mod8source',247,759,0,26)
	Parameter('mod8amount',248,760,0,254)
	Parameter('mod8destination',249,761,0,97)
	Parameter('mod9source',251,763,0,26)
	Parameter('mod9amount',252,764,0,254)
	Parameter('mod9destination',253,765,0,97)
	Parameter('mod10source',255,767,0,26)
	Parameter('mod10amount',256,768,0,254)
	Parameter('mod10destination',257,769,0,97)
	Parameter('mod11source',259,771,0,26)
	Parameter('mod11amount',260,772,0,254)
	Parameter('mod11destination',261,773,0,97)
	Parameter('mod12source',263,775,0,26)
	Parameter('mod12amount',264,776,0,254)
	Parameter('mod12destination',265,777,0,97)
	Parameter('mod13source',267,779,0,26)
	Parameter('mod13amount',268,780,0,254)
	Parameter('mod13destination',269,781,0,97)
	Parameter('mod14source',271,783,0,26)
	Parameter('mod14amount',272,784,0,254)
	Parameter('mod14destination',273,785,0,97)
	Parameter('mod15source',275,787,0,26)
	Parameter('mod15amount',276,788,0,254)
	Parameter('mod15destination',277,789,0,97)
	Parameter('mod16source',279,791,0,26)
	Parameter('mod16amount',280,792,0,254)
	Parameter('mod16destination',281,793,0,97)
	Parameter('unison',283,795,0,1)
	Parameter('unisondetune',284,796,0,127)
	Parameter('unisonmode',285,797,0,1)
	Parameter('unisonkeyassign',286,798,0,5)
	Parameter('splitpoint',287,287,0,127)
	Parameter('abmode',288,288,0,2)
	Parameter('arpeggiator',289,801,0,1)
	Parameter('arpeggiatormode',290,802,0,4)
	Parameter('arpeggiatorrange',291,803,0,2)
	Parameter('arpclockdivide',292,804,0,10)
	Parameter('arpeggiatorrepeats',293,805,0,3)
	Parameter('arpautolatch',294,806,0,1)
	Parameter('arplockonoff',295,807,0,1)
	Parameter('bpm',288,800,30,250)
	Parameter('arpnote1',301,813,0,127)
	Parameter('arpnote2',302,814,0,127)
	Parameter('arpnote3',303,815,0,127)
	Parameter('arpnote4',304,816,0,127)
	Parameter('arpnote5',305,817,0,127)
	Parameter('arpnote6',306,818,0,127)
	Parameter('arpnote7',307,819,0,127)
	Parameter('arpnote8',308,820,0,127)
	Parameter('arpnote9',309,821,0,127)
	Parameter('arpnote10',310,822,0,127)
	Parameter('arpnote11',311,823,0,127)
	Parameter('arpnote12',312,824,0,127)
	Parameter('arpnote13',313,825,0,127)
	Parameter('arpnote14',314,826,0,127)
	Parameter('arpnote15',315,827,0,127)
	Parameter('arpnote16',316,828,0,127)
	Parameter('arpnote17',317,829,0,127)
	Parameter('arpnote18',318,830,0,127)
	Parameter('arpnote19',319,831,0,127)
	Parameter('arpnote20',320,832,0,127)
	Parameter('arpnote21',321,833,0,127)
	Parameter('arpnote22',322,834,0,127)
	Parameter('arpnote23',323,835,0,127)
	Parameter('arpnote24',324,836,0,127)
	Parameter('arpnote25',325,837,0,127)
	Parameter('arpnote26',326,838,0,127)
	Parameter('arpnote27',327,839,0,127)
	Parameter('arpnote28',328,840,0,127)
	Parameter('arpnote29',329,841,0,127)
	Parameter('arpnote30',330,842,0,127)
	Parameter('arpnote31',331,843,0,127)
	Parameter('arpnote32',332,844,0,127)
	Parameter('arpvelocity1',333,846,0,127)
	Parameter('arpvelocity2',334,847,0,127)
	Parameter('arpvelocity3',335,848,0,127)
	Parameter('arpvelocity4',336,849,0,127)
	Parameter('arpvelocity5',337,850,0,127)
	Parameter('arpvelocity6',338,851,0,127)
	Parameter('arpvelocity7',339,852,0,127)
	Parameter('arpvelocity8',340,853,0,127)
	Parameter('arpvelocity9',341,854,0,127)
	Parameter('arpvelocity10',342,855,0,127)
	Parameter('arpvelocity11',343,856,0,127)
	Parameter('arpvelocity12',344,857,0,127)
	Parameter('arpvelocity13',345,858,0,127)
	Parameter('arpvelocity14',346,859,0,127)
	Parameter('arpvelocity15',347,860,0,127)
	Parameter('arpvelocity16',348,861,0,127)
	Parameter('arpvelocity17',349,862,0,127)
	Parameter('arpvelocity18',350,863,0,127)
	Parameter('arpvelocity19',351,864,0,127)
	Parameter('arpvelocity20',352,865,0,127)
	Parameter('arpvelocity21',353,866,0,127)
	Parameter('arpvelocity22',354,867,0,127)
	Parameter('arpvelocity23',355,868,0,127)
	Parameter('arpvelocity24',356,869,0,127)
	Parameter('arpvelocity25',357,870,0,127)
	Parameter('arpvelocity26',358,871,0,127)
	Parameter('arpvelocity27',359,872,0,127)
	Parameter('arpvelocity28',360,873,0,127)
	Parameter('arpvelocity29',361,874,0,127)
	Parameter('arpvelocity30',362,875,0,127)
	Parameter('arpvelocity31',363,876,0,127)
	Parameter('arpvelocity32',364,877,0,127)
]

ParameterDict = {p.name:p for p in ParameterList}
