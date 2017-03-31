#!/usr/bin/python

import media

toy_story = media.Movie("Toy story", "a story of a boy and his toys that come to life","https://en.wikipedia.org/wiki/File:Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)
#print(toy_story.title)

avatar = media.Movie("Avatar", "A Marine on an Alien Planet","https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=aVdO-cx-McA")
#print(avatar.storyline)
#avatar.show_trailer()
ShawShank = media.Movie("The Shawshank Redemption", "Fear can hold you prisoner Hope can set you free.","https://en.wikipedia.org/wiki/The_Shawshank_Redemption#/media/File:ShawshankRedemptionMoviePoster.jpg","https://www.youtube.com/watch?v=6hB3S9bIaco")


print(ShawShank.storyline)
ShawShank.show_trailer()
