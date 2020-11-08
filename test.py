#Create a podcast selection list of podcast dictionaries, with podcast name and URL as key and value pairs
#Create an empty list for the picked podcasts to be added to
#Remove the podcast from the selection
#Pick a podcast from the selection at random
#Add it to the picked podcasts 

from random import choice

podcast_selection = [{"The Allusionist": "URL"}, {"No Such Thing as a Fish": "URL"}, {"Work In Sanity": "URL"}, {"Do By Friday": "URL"}]
picked_podcasts = []

chosen_podcast = choice(podcast_selection)
print(chosen_podcast)

picked_podcasts.append(chosen_podcast)
podcast_selection.remove(chosen_podcast)

print(podcast_selection)
print(picked_podcasts)