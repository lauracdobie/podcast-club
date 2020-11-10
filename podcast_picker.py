from random import choice

my_podcast_file = open("podcast_selection.txt", "r")

podcast_list = my_podcast_file.readlines()
my_podcast_file.close()

podcast_selection = []
for podcast in podcast_list: 
	podcast_selection.append(podcast.replace("\n", ""))

my_podcast_file_2 = open("picked_podcasts.txt", "r")

podcast_list_2 = my_podcast_file_2.readlines()
my_podcast_file_2.close()

picked_podcasts = []
for podcast in podcast_list_2: 
	picked_podcasts.append(podcast.replace("\n", ""))

print("Podcast selection:")
for podcast in podcast_selection:
    print(podcast)
print(" ")


chosen_podcast = choice(podcast_selection)
print("Today's random pick is:")
print(chosen_podcast)
print(" ")

podcast_selection.remove(chosen_podcast)
picked_podcasts.append(chosen_podcast)

rewrite_data = open("podcast_selection.txt", "w+")

for podcast in podcast_selection:
	rewrite_data.write(podcast+"\n")

rewrite_data.close()

rewrite_data_2 = open("picked_podcasts.txt", "w+")

for podcast in picked_podcasts:
	rewrite_data_2.write(podcast+"\n")

rewrite_data_2.close()

print("Picked podcasts so far:")
for podcast in picked_podcasts:
    print(podcast)
print(" ")
