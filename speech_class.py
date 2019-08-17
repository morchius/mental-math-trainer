# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 22:36:43 2019

@author: Claudius
"""

import win32com.client

class Speaker():
	def __init__(self):
		self._speak = win32com.client.Dispatch('Sapi.SpVoice')

	def get_voices(self, arg=None):
		c = self._speak.getVoices
		voices = c() if arg is None else c(arg)
		return [voices.Item(i).getDescription() for i in range(voices.count)]
	
	def speak(self, text):
		self._speak.Speak(text)
	
	def _set_voice(self, voice):
		voices = self._speak.getVoices('Name='+voice)
		if not voices.count:
			raise ValueError('unknown voice: ' + str(voice))
		self._speak.Voice = voices.item(0)
	def _get_voice(self):
		return self._speak.voice.getDescription()
		
	
	def _mkprop(attr):
		def setter(self, val):
			self._speak.__setattr__(attr, val)
		def getter(self):
			return
		return property(getter, setter)
	
	voice = property(_get_voice, _set_voice)
	volume = _mkprop('Volume')
	rate = _mkprop('Rate')

def main():
	text = "mein name ist bender, bitte diskette einlegen"

	s = Speaker()
	s.voice = "Microsoft Zira Desktop"
	s.volume = 100
	print(s.get_voices())
	s.speak(text)

if __name__ == "__main__":
	main()