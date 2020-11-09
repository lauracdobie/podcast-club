#Create a podcast selection list of podcast dictionaries, with podcast name and URL as key and value pairs
#Create an empty list for the picked podcasts to be added to
#Remove the podcast from the selection
#Pick a podcast from the selection at random
#Add it to the picked podcasts 
import csv
from random import choice

podcast_selection = []
picked_podcasts = []

with open('podcast_selection.csv') as csvfile:
    podcasts = csv.reader(csvfile, delimiter=',')
    for podcast in podcasts:
        podcast_selection.append(podcast)

print("Podcast selection")
for podcast in podcast_selection:
    print(podcast)
print(" ")


chosen_podcast = choice(podcast_selection)
print("Today's random pick is:")
print(chosen_podcast)
print(" ")

podcast_selection.remove(chosen_podcast)

# chosen_podcast_index = podcast_selection.index(chosen_podcast)
# print(chosen_podcast_index)

with open('picked_podcasts.csv', mode="a") as csvfile:
    chosen = csv.writer(csvfile, delimiter=',')
    chosen.writerow(chosen_podcast)

with open('picked_podcasts.csv') as csvfile:
    chosen = csv.reader(csvfile, delimiter=',')
    for podcast in chosen:
        picked_podcasts.append(podcast)

# with open('podcast_selection.csv', mode="a") as csvfile:
#     writer = csv.writer(csvfile, delimiter=',')
#     writer.writerows(podcast_selection)

# with open('podcast_selection.csv', mode="a") as csvfile:
#     writer = csv.writer(csvfile, delimiter=',')
#     podcasts = csv.reader(csvfile, delimiter=',')
#     for podcast in podcasts:
#         if podcast == chosen_podcast:
#             writer.writerow(chosen_podcast)

print("Picked podcasts so far:")
for podcast in picked_podcasts:
    print(podcast)
print(" ")

