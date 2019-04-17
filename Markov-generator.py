#!/usr/bin/python3
import requests
import sys
import os
import hashlib
import lyricwikia
from pymarkovchain import MarkovChain

API_URI = "http://lyrics.wikia.com/api.php?action=lyrics&fmt=realjson"

file = open("lyrics.txt", "w")

if __name__ == '__main__':

	if len(sys.argv) != 3:
		raise "Usage: python3 py-simple-lyric-generator \"[artist_name]\" [number_of_phrases_to_generate]"

	artist_name = sys.argv[1]
	number_of_phrases = sys.argv[2]
	params = {
		'artist': artist_name
	}

	# Generating a Markov Chain Model
	db_name_hashed = "db/" + hashlib.md5(artist_name.lower().encode('utf-8')).hexdigest()
	mc = MarkovChain(db_name_hashed)
	
	file.write("----------------- Lyrics for artist: " + artist_name + "-----------------\n");

	# Checking if the database already exists, if so uses the cache instead another API call
	if not os.path.isfile(db_name_hashed):
		print("No data cached. Please be patient while we search the lyrics of %s." % artist_name)		
		
		# Adding lyrics to a single gigant string
		lyrics = ''

		# Parsing each lyric from this artist.
		# [http://api.wikia.com/wiki/LyricWiki_API]
		artist = requests.get(API_URI, params=params).json()
		for album in artist['albums']:
			for song in album['songs']:
				params = {
					'artist': artist_name,
					'song': song
				}
				print("Parsing \"{}\" from Wikia.".format(song))
				response = requests.get(API_URI, params=params).json()["lyrics"]
				lyrics += response.replace('[...]', '') + ' '
				
				#Some of the lyrics were missing using lyricwikia which were causing errors
				#Programmed to skip the songs whose lyrics weren't available
				try:
					file.write("\n\n----------------- Song name: " + song + " -----------------\n\n")
					text_lyrics = lyricwikia.get_lyrics(artist_name, song)
					file.write(text_lyrics)
				except:
					print("Lyrics for " + song + " not found, skipping.......")
					file.write("Lyrics not found for " + song + " :(\n")

		# Generating the database
		mc.generateDatabase(lyrics)
		mc.dumpdb()
		file.write("\n\n----------------- End of lyrics for " + artist_name +" -----------------\n\n")
		file.close()
	# Printing a string
	for i in range(0, int(number_of_phrases)):
		print(mc.generateString())
