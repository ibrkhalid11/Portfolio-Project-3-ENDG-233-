
# spotify_program.py
# IBRAHIM KHALID, ENDG 233 F23
# A terminal-based application to process and plot data based on given user input and provided data values.
# You may only import numpy, matplotlib, and math.
# No other modules may be imported. Only built-in functions that support compound data structures, user entry, or casting may be used.
# Remember to include docstrings for any functions/classes, and comments throughout your code.
#

import numpy as np
import matplotlib.pyplot as plt

# ******************************************************************************************************
# Data is imported from the included csv file. You may not modify the content, order, or location of the csv file.
# Do not modify the code in this section.
# You may not hardcode (manually enter in the code) any other data.
column_names = ['title', 'artist(s)', 'release', 'num_of_streams', 'bpm', 'key', 'mode', 'danceability', 'valence', 'energy', 'acousticness', 'instrumentalness', 'liveness', 'speechiness']
data = np.genfromtxt('spotify_data.csv', delimiter = ',', skip_header = True, dtype = str)
# ******************************************************************************************************


# ******************************************************************************************************
# DEFINE BONUS CLASS HERE (optional)
class Song:
    '''
    Class used to obtain stats from a specified song from the user

        Attributes:
            title(str): String that is the name of the song as it appears on Spotify.
            artist(str): String that represents the names of the artists inolved
            release(float): Float value that represents the year that the song was released
            num_of_streams(float): Float value that represents the number of times the song was streamed
            bpm(float): Float value that represents the measurement of musical tempo of the song
            key(str): String that represents the scale of the song
            mode(str): String that represents the modal scale of the song
            danceability(float): Float that represents the percentage that indicates how suitable the song is for dancing
            valence(float): Float that represents valence: Percieved positivity of the song's musical content (percentage)
            energy(float): Float as a percentage that represents percieved energy of the song
            acousticness(float): Float as a percentage that represents amount of acoustic noise in the song
            instrumentalness(float): Float that represents the amount of instrumental content in the song
            liveness(float): Float that represents the amount of live performance elements shown as a percentage
            speechiness(float): Float that represents the amount of spoken words in the song 
            percentages(int): List of the above attributes and their values
    '''

    '''
    __init__ is a function that is meant 
    '''
    def __init__(self, title, artist, release, num_of_streams, bpm, key, mode,
                danceability, valence, energy, acousticness, instrumentalness, liveness, speechiness, percentages):
        self.title = title
        self.release = release
        self.artist = artist
        self.num_of_streams = num_of_streams
        self.bpm = bpm
        self.key = key
        self.mode = mode
        self.danceability = danceability
        self.valence = valence
        self.energy = energy
        self.acousticness = acousticness
        self.instrumentalness = instrumentalness
        self.liveness = liveness
        self.speechiness = speechiness
        self.percentages = [float(data[percentages][column_names.index('danceability')]), float(data[percentages][column_names.index('valence')]), float(data[percentages][column_names.index('energy')]),
                            float(data[percentages][column_names.index('acousticness')]), float(data[percentages][column_names.index('instrumentalness')]), float(data[percentages][column_names.index('liveness')]),
                            float(data[percentages][column_names.index('speechiness')])]
# ******************************************************************************************************
# DEFINE FUNCTIONS HERE
'''
feature_stats is a function that uses the parameter value to determine the features highest and lowest value in the dataset provided
this is done by making an array of each feature and using the parameter to specify which column of the array/feature to use in its calculations
outputs: highest value, lowest value, mean value, top song(done through last_index) 
'''
def feature_stats(value):
    feature_container = np.array([row[value] for row in data], dtype = np.int64)
    #find column that contains the feature stats of each song, then sets it into an array
    print(f'Highest value: {(max(feature_container))}')
    #find max of the feature
    print(f'Lowest value: {(min(feature_container))}')
    #find min of each featyre
    print(f'Mean value: {int((np.mean(feature_container)))}')
    #find mean value of said feature from array
    last_index = np.argmax(feature_container)
    return last_index

'''
age_stats is a function that considers the users input as a parameter and will determine the oldest song, 
as well as calculate the span of years between the oldest song and the latest song in the csv file
it will also provide the artist of the oldest song, as well as it's key and mode
'''
def age_stats(value):
    #finds the column that contains the release year of each song; then sets it into an array
    years = np.array([i[column_names.index('release')] for i in data], dtype = np.int64)
    #takes the maximum and minimum value of the above array and then finds the difference to find the amount of years between the oldest song and the newest
    print(f'Span of years: {(max(years)) - (min(years))}')
    #finds the corresponding row of the oldest year entry, then finds the 'artists' column and retrieves that entry to display
    print('Artist of oldest song:', data[np.argmin(years)][column_names.index('artist(s)')])
    #same logic as above piece of code; finds corresponding row of oldest year entry, then retrieves the values from the 'key' and 'mode' index
    print('Key and mode of oldest song:', data[np.argmin(years)][column_names.index('key')], data[np.argmin(years)][column_names.index('mode')])
'''
graphing_function is a function with no required parameters, 
which is called upon when the user input from main() is -1. 
This function will take in the data given in the csv file,
specifically from the BPM and danceability columns, 
and will graph all entries of it 
'''
def graphing_function() :
    #finds the column that contains the BPM of each song, then sets it into an array
    beats_per_min = np.array([columns[column_names.index('bpm')] for columns in data], dtype='float')
    #finds the column that contains the danceability of each song, then sets it into an array
    danceability = np.array([columns[column_names.index('danceability')] for columns in data], dtype='float')
    #sizes the plots length and width
    plt.figure(figsize = [16,9])
    #creates a scatter plot graph of the following two arrays (x-axis=BPM, y-axis=danceability)
    plt.scatter(beats_per_min, danceability, s=10, c = 'b')
    #label y axis as 'danceability'
    plt.ylabel('Danceability')
    #label x axis as 'BPM'
    plt.xlabel('BPM')
    #creates title of the scatterplot
    plt.title('Danceability vs. Beats per Minute')
    #label legend as song stats
    plt.legend(['Song Stats'])
    #show scatterplot
    plt.savefig('song_stats_graph.png')
    plt.show()
# ******************************************************************************************************
# DEFINE MAIN CODE
# Add your code within the main function. A docstring is not required for this function.
# You may find the following hints helpful:
# A list comprehension can be used to convert data values in a column and create a new array
# e.g. converted_data = np.array([row[column_value] for row in data], dtype='float')
# NumPy has many built-in functions/methods, including those for finding the index location of a value (e.g. argmax(), argmin(), etc.)
# Refer to the NumPy and Matplotlib documentation for more
'''
main is the function that will primarily be used in this program. It's first function is to provide a menu for the user to access
This function does not have a parameter and it is not returning anything once the function is completed.
Major aspects: if input is -1, a graph of the beats per minute and danceability is shown, and then another bar graph of the stats of a song that the user enters the row number of
               if the input is in the unusable list, it prompts again for input
               if the input is in the usable list, it calls
'''
def main():
    print("ENDG 233 Spotify Statistics\n")
    print("Song analysis options: ")
    for menu, option in enumerate(column_names):
        print(menu, option)
    print("Choose -1 to end the program.")

    # Continue main code below
    #prompt the user for a number corresponding to the feature they want to analyze.
    user_input = int(input('\nPlease enter a song feature to analyze: '))

    #two lists of numbers, one which contains the numbers for features that will be analyzed, and the other for features that will not be
    #leading to the program skipping it and prompting the user for input once again.

    #numbers that can be used by feature_stats() function, hence why 2 is not appearing
    useable_vals = [3, 4, 7, 8, 9, 10, 11, 12, 13]
    #numbers that are meant to be skipped
    cannot_use_these_vals = [0, 1, 5, 6]

    #as long as user_input is not -1, we can keep prompting the user with entering song features
    while user_input != -1:
        #if user inputs 2, call age_stats
        if user_input == 2:
            #
            age_stats(user_input)
        #if user_input in useable numbers, call feature_stats to determine statistics of wanted feature
        elif user_input in useable_vals:
        #print top song, call function
            print(f'Top song in selected feature: {data[feature_stats(user_input)][0]}')
        
        #if user_input is in the unuseable list
        elif user_input in cannot_use_these_vals:
        #skip and break the loop
            pass
        else:
        #if user_input is not in either list, and not 2 or -1
            print('You must enter a valid menu option.')
        #this finishes the loop, calls user_input prompt again
        user_input = int(input('\nPlease enter a song feature to analyze: '))
    #breaks out of while loop, calls plotting function when user inputs -1 when prompted
    graphing_function()

    # Create and print danceability vs. bpm plot
    #using the new class, it is used and each attribute is assigned a value which is the value of each feature for the selected row
    song = int(input('Bonus - Enter any row number: '))
    #after seeing first plot, user is prompted to enter a row number to display the bonus plot
    song_plot = Song(str(data[song][column_names.index('title')]), str(data[song][column_names.index('artist(s)')]), float(data[song][column_names.index('release')]), float(data[song][column_names.index('num_of_streams')]), float(data[song][column_names.index('bpm')]), str(data[song][column_names.index('key')]),
                     str(data[song][column_names.index('mode')]), float(data[song][column_names.index('danceability')]), float(data[song][column_names.index('valence')]), float(data[song][column_names.index('energy')]),
                     float(data[song][column_names.index('acousticness')]), float(data[song][column_names.index('instrumentalness')]), float(data[song][column_names.index('liveness')]), float(data[song][column_names.index('speechiness')]), song)
    #
    #create an array with the names of each feature to be featured on the plot
    bar_graph_array_numbers = np.array(['danceability', 'valence', 'energy', 'acousticness', 'instrumentalness', 'liveness', 'speechiness'])
    #create array of first row, used for x-axis of bar plot
    #get the name of the song for the title of the plot
    song_name = (data[song][column_names.index('title')])
    #find each entry in the 'title' column
    plt.figure(figsize = [16, 9])

    #keep the figure size the same from the scatter plot
    plt.ylim([0, 100])

    #make a bar chart using the names from bar_graph_array_numbers and the percentages from the percentages attribute in the class Song
    plt.bar(bar_graph_array_numbers, song_plot.percentages)
    plt.title(f'Song stats for {song_name}')
    plt.savefig('Bonus_Graph.png')
    plt.show()
'''
if this file is the main one, run main()
'''
if __name__ == '__main__':
    main()