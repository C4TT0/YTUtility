# Imports 

import sys
import os
import re
import random
import pafy
import random
from pytube import Playlist
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
		except Exception as e:
			print("[+] An Unkown error occurred: ", e)

	def downloadplaylist(self, link):
		try:
			self.randNum = random.randint(0, 99999)
			self.dirName = "Playlist" + str(self.randNum)
			self.cwd = os.getcwd()
			self.path = os.path.join(self.cwd, self.dirName)

			try:
				os.mkdir(self.path)
			except FileExistsError as e:
				print("[-] Folder Already Exsists")

			print("[+] Downloading Playlist")

			self.p = Playlist(link)
			for video in range(0, len(self.p)):
				self.vid = pafy.new(self.p[video])
				self.bestRes = self.vid.getbest()
				self.bestRes.download(r'{}'.format(self.dirName + "/"))

			print("[+] Download Complete")

		except Exception as e:
			print("[+] An Unkown error occurred ", e)

# Main Class

class Main:
	def __init__(self):
		self.banner = """ 
		=======================
		[+] Youtube Utility [+]
		=======================

		[ 1 ] Download Youtube Video [ Link ]
		[ 2 ] Download Youtube Video and Convert it to Audio [ Link ]
		[ 3 ] Download Youtube Playlist ( Make sure that the playlist is public ) [ Link ]
		[ 4 ] Download Youtube Playlist and Convert it to Audio ( Make sure that the playlist is public ) [ Link ]
		[ 5 ] Gather Youtube Video Data
		[ 6 ] Youtube Search For Audio Download
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
				Utility().downloadplaylist("https://www.youtube.com/playlist?list=PLAyZZFqXfE53WOsDdpw0H3wsdIITSPb07")

			elif self.urlInput == "4":
				print("4")

			elif self.urlInput == "5":
				print("5")

			else:
				print("[-] Please Make a valid choice !")


if __name__ == '__main__':
	App = Main()
	App.work()