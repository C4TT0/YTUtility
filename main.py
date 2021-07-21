# Imports 

import sys
import os
import re
import random
import pafy
import random
import urllib.request
from pytube import Playlist
from hurry.filesize import verbose, size
import moviepy.editor as mp

# Utility Class which will perform main functions

class Utility:
	def __init__(self):
		pass

	# Function to download youtube video

	def downloadytvid(self, link):
		try:
			# Download youtube video
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

	# Function to convert a youtube video to audio

	def downloadnconvytvid(self, link):
		try:
			# Download youtube video
			self.video = pafy.new(link)
			self.bestResolutionVideo = self.video.getbest()
			self.videoName = str(self.video.title) + ".mp4"
			self.videoSize = self.bestResolutionVideo.get_filesize()
			self.videoSizeInMb = size(self.videoSize, system=verbose)
			print("[+] Downloading {}".format(self.videoName))
			print("[+] Size: {}".format(self.videoSizeInMb))
			self.bestResolutionVideo.download('./Video/')
			print("[+] Download Complete !", "\n")
			# Convert video to audio
			print("[+] Converting Video to Audio")
			self.videoFile = mp.VideoFileClip(r"./Video/" + self.videoName)
			self.songName = str(self.video.title) + ".mp3"
			self.videoFile.audio.write_audiofile(r"./Audio/" + self.songName)
			print("[+] Converison Complete !")
			# Remove the video
			print("[+] Cleaning Up")
			os.remove('./Video/' + self.videoName)

			print("[+] Done !")

		except Exception as e:
			print("[+] An Unkown error occurred: ", e)

	# Function to download Youtube Playlist

	def downloadplaylist(self, link):
		try:
			# Creating a name and path for playlist
			self.randNum = random.randint(0, 99999)
			self.dirName = "Playlist" + str(self.randNum)
			self.cwd = os.getcwd()
			self.path = os.path.join(self.cwd, self.dirName)

			try:
				os.mkdir(self.path)
			except FileExistsError as e:
				print("[-] Folder Already Exsists")

			# Downloading songs of playlist

			print("[+] Downloading Playlist")

			self.p = Playlist(link)
			for video in range(0, len(self.p)):
				self.vid = pafy.new(self.p[video])
				self.bestRes = self.vid.getbest()
				self.bestRes.download(r'{}'.format(self.dirName + "/"))

			print("[+] Download Complete")

		except Exception as e:
			print("[+] An Unkown error occurred ", e)

	# Function to Convert a youtube playlist to audio

	def convertplaylisttoaudio(self, link):
		try:
			# Creating a name and path for playlist
			self.randNum = random.randint(0, 99999)
			self.dirName = "Playlist" + str(self.randNum)
			self.cwd = os.getcwd()
			self.path = os.path.join(self.cwd, self.dirName)

			try:
				os.mkdir(self.path)
			except FileExistsError as e:
				print("[-] Folder Already Exsists")

			# Downloading songs of playlist

			print("[+] Downloading Playlist")

			self.p = Playlist(link)
			for video in range(0, len(self.p)):
				self.vid = pafy.new(self.p[video])
				self.bestRes = self.vid.getbest()
				self.bestRes.download(r'{}'.format(self.dirName + "/"))

			print("[+] Download Complete")

			# Converting Playlist to Audio

			print("[+] Converting To Audio")

			f = []

			for (filename) in os.walk(self.dirName):
				f.extend(filename)

			for i in range(0, len(f[2])):
				self.videoFile = mp.VideoFileClip(self.dirName + "/" + f[2][i])
				self.songName = str(f[2][i]).split(".mp4")[0] + ".mp3"
				self.videoFile.audio.write_audiofile(self.dirName +  "/" + self.songName)

			print("[+] Conversion complete")

			# Cleaning things up

			print("[+] Cleaning things up")

			dir_ = self.dirName
			ext = r".mp4"

			for _ in os.listdir(dir_):
				if _.endswith(ext):
					os.remove(dir_ + "/" + _)

			print("[+] Done")
			

		except Exception as e:
			print("[+] An Unkown error occurred ", e)

	# Function to search youtube and download song and convert it to audio

	def searchnconv(self, link):
		link = link.replace(" ", "+")
		html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={link}")
		video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
		list_of_ids = []

		for i in range(0, 4):
		    v = pafy.new(video_ids[i])
		    print( f"[ {i} ] " + str(v.title) + " By" + " " + str(v.author) + " " + str(v.duration) + " Long" + " " + str(v.viewcount) + " Views")
		    list_of_ids.append(video_ids[i])

		choice = int(input("[+] Choose one: "))

		finalUrl = "https://www.youtube.com/watch?v=" + list_of_ids[choice]

		print("[+] Target URL: ", finalUrl)

		print("[+] Downloading Video")

		self.video = pafy.new(finalUrl)
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

		print("[+] Cleaning things up ")
		os.remove("./Video/" + self.videoName)

		print("[+] Done")


# Main Class

class Main:
	def __init__(self):
		# Tool Banner

		self.banner = """ 
		=======================
		[+] Youtube Utility [+]
		=======================

		[ 0 ] Help
		[ 1 ] Download Youtube Video [ Link ]
		[ 2 ] Convert Youtube Video to Audio [ Link ]
		[ 3 ] Download Youtube Playlist ( Make sure that the playlist is public ) [ Link ]
		[ 4 ] Convert Youtube Playlist to Audio ( Make sure that the playlist is public ) [ Link ]
		[ 5 ] Youtube Search For Audio Download
		[ 99 ] Exit

		Made By Typh0n12
		Github: https://github.com/Typh0n12
		"""

	def work(self):
		print(self.banner)
		
		# Regex for checking for a legimate youtube video link

		self.youtubevid_regex = re.compile(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})')

		# Regex for checking for a legimate youtube playlist link

		self.youtubeplay_regex = re.compile(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(playlist\?list=|embed/|v/|.+\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})')
		
		# Running a loop for user input

		while True:
			self.urlInput = str(input(">>> "))

			# Checking if the link is valid or not in every conditional statement

			if self.urlInput == "99":
				msg = ['Have a Good Day Bye', 'Adios', 'Exitting.....']
				print(msg[random.randint(0, 2)])
				sys.exit(0)

			elif self.urlInput == "0":
				print(self.banner)

			elif self.urlInput == "1":
				self.input = str(input("[+] Enter youtube Video Link: "))
				match = self.youtubevid_regex.findall(self.input)
				if not match:
					print("[-] Please enter a valid youtube video link !")
				else:
					Utility().downloadytvid(self.input)

			elif self.urlInput == "2":
				self.input = str(input("[+] Enter youtube Video Link: "))
				match = self.youtubevid_regex.findall(self.input)
				if not match:
					print("[-] Please enter a valid youtube video link !")
				else:
					Utility().downloadnconvytvid(self.input)

			elif self.urlInput == "3":
				self.input = str(input("[+] Enter youtube playlist link: "))
				match = self.youtubeplay_regex.findall(self.input)
				if not match:
					print("[-] Please enter a valid youtube playlist link !")
				else:
					Utility().downloadplaylist(self.input)

			elif self.urlInput == "4":
				self.input = str(input("[+] Enter youtube playlist link: "))
				match = self.youtubeplay_regex.findall(self.input)
				if not match:
					print("[-] Please enter a valid youtube playlist link !")
				else:
					Utility().convertplaylisttoaudio(self.input)

			elif self.urlInput == "5":
				self.input = str(input("[+] Search Query: "))
				Utility().searchnconv(self.input)

			else:
				print("[-] Please Make a valid choice !")


if __name__ == '__main__':
	App = Main()
	App.work()
