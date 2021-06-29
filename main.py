# Imports 

import sys
import re
import random
import pafy
from hurry.filesize import verbose, size
import moviepy.editor as mp

# Utility Class which will perform main functions

class Utility:
	def __init__(self):
		pass

	def downloadytvid(self, link):
		try:
			self.video = pafy.new(link)
			self.bestResolutionVideo = self.video.getbest()
			self.videoName = str(self.video.title) + ".mp4"
			self.videoSize = self.bestResolutionVideo.get_filesize()
			self.videoSizeInMb = size(self.videoSize, system=verbose)
			print("[+] Downloading {}".format(self.videoName))
			print("[+] Size: {}".format(self.videoSizeInMb))
			self.bestResolutionVideo.download('./Video/')
			print("[+] Download Complete !", "\n")
		except Exception as e:
			print("[-] This Video Already exsists")
			print(e)

	def downloadnconvytvid(self, link):
		try:
			self.video = pafy.new(link)
			self.bestResolutionVideo = self.video.getbest()
			self.videoName = str(self.video.title) + ".mp4"
			self.videoSize = self.bestResolutionVideo.get_filesize()
			self.videoSizeInMb = size(self.videoSize, system=verbose)
			print("[+] Downloading {}".format(self.videoName))
			print("[+] Size: {}".format(self.videoSizeInMb))
			self.bestResolutionVideo.download('./Video/')
			print("[+] Download Complete !", "\n")

			print("[+] Converting Video to Audio")
			self.videoFile = mp.VideoFileClip(r"./Video/" + self.videoName)
			self.songName = str(self.video.title) + ".mp3"
			self.videoFile.audio.write_audiofile(r"./Audio/" + self.songName)
			print("[+] Converison Complete !")

# Main Class

class Main:
	def __init__(self):
		self.banner = """ 
		=======================
		[+] Youtube Utility [+]
		=======================

		[ 1 ] Download Youtube Video
		[ 2 ] Download Youtube Video and Convert it to Audio
		[ 3 ] Download Youtube Playlist
		[ 4 ] Download Youtube Playlist and Convert it to Audio
		[ 5 ] Gather Youtube Video Data
		[ 99 ] Exit

		Made By Typh0n12
		Github: https://github.com/Typh0n12
		"""

	def work(self):
		print(self.banner)
		while True:
			self.urlInput = str(input(">>> "))

			if self.urlInput == "99":
				msg = ['Have a Good Day Bye', 'Adios', 'Exitting.....']
				print(msg[random.randint(0, 2)])
				sys.exit(0)

			elif self.urlInput == "1":
				pass
				# self.url = str(input("[+] Enter Youtube Video Link: "))
				# Utility().downloadytvid(self.url)

			elif self.urlInput == "2":
				print("2")

			elif self.urlInput == "3":
				print("3")

			elif self.urlInput == "4":
				print("4")

			elif self.urlInput == "5":
				print("5")

			else:
				print("[-] Please Make a valid choice !")


if __name__ == '__main__':
	App = Main()
	App.work()