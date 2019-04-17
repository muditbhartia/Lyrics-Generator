# Lyrics-Generator
An application that uses an artist or band’s lyrics to generate “new” similar-sounding lyrics based on probabilities. New Lyrics would be generated based on a particular artist’s lyrics using Markov chains.


### Introduction

Nowadays many song writers in the music industry have started using various tools to help them write songs. Our attempt in this project is to create one such tool which would help these writers to generate new lyrics based on a database of old lyrics.
I would be using Markov chain for making this Lyrics generator. It is generated from some text based on the frequency of certain patterns occurring.
I will be using PyMarkovChain python library for markov chain text generation, hashed database for caching and lyricswikia library for corpora generation.

### Methodolgy

This small project generate new lyrics based on the lyrics of a given artist. For example, you can ask the script to generate Pink Floyd-like lyrics, so it will read all the lyrics from Pink Floyd and generate a new one with the same style.
I've made a "database" too, so whenever you load all lyrics from a given artist it will be saved on your computer under the *db* folder. This way we can avoid a lot of API calls (since they are quite expensive).
For our datasets we will use APIs from songs website to get the lyrics online. We would use individual words as our tokens rather than taking things character by character. For adding in the Markov chain functionality we use pymarkovchain pakage in python.
After we’ve received a lyrics response from the API, we simply create a MarkovChain, load in the lyrics data, and generate a list of sentences.

### Design

<img width="446" alt="Screenshot 2019-04-17 at 10 12 17 PM" src="https://user-images.githubusercontent.com/45623734/56305433-eb5b6900-615d-11e9-876d-f2a357fb8c04.png">

### How to Run the Code

First in order run the python code use the following command, you have to pass 2 arguments namely the Artist Name and the number of lines of lyrics you want to generate
```
$ python Markov-generator.py coldplay 10
```
Here I have given Artist name as Coldplay and 10 as the number of lines of lyrics


#### Now when you run the code for the first time for a particular artist you will see that the code parses lyrics as JSON objects from lyricswikea. When you again try to run the code for the same artist, you will notice that the code will directly produce the output. This is due to the caching of the lyrics in the hashed database. 

#### NOTE: 

* Also for reference I am writing the lyrics of the artist taken from the API and saving it in the lyrics.txt file to analyse the generated lyrics with the corpus.

* All the screenshots for running the code along with the output generated have been given in the Screenshot directory under this repository. 

