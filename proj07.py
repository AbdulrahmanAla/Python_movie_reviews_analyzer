###########################################################################################################################################
##
## Source Code
##
## Programming Project #7 
##
## prompts the user to input a file name to open and keeps prompting until a correct name is entered
##   
## reads the file and returns a list of tuples
##
## list the users in tuples with each tuple contain (age, gender, occupation)
##
## list the users with their ratings
##
## list the name of the movie with the date and the indciated categories as list
##
## filter the movie based on the year, genre, gender and occuption
##
## filter the movie based on the highest rating
##
## filter the movie based on the highest reviewer
##
###########################################################################################################################################
GENRES = ['Unknown','Action', 'Adventure', 'Animation',"Children's",
          'Comedy','Crime','Documentary', 'Drama', 'Fantasy', 'Film-noir',
          'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 
          'War', 'Western']
OCCUPATIONS = ['administrator', 'artist', 'doctor', 'educator', 'engineer',
               'entertainment', 'executive', 'healthcare', 'homemaker', 'lawyer',
               'librarian', 'marketing', 'none', 'other', 'programmer', 'retired',
               'salesman', 'scientist', 'student', 'technician', 'writer']
'''
Three main data structures (lists)
L_users, indexed by userID, list of tuples (age,gender,occupation)
L_reviews, indexed by userID, list of tuples (movieID, rating)
L_movies, indexed by movieID, list of tuples (movieName, releaseDate, list of genres)
'''
MENU = '''
        Options:
        1. Highest rated movie for a specific year
        2. Highest rated movie for a specific Genre
        3. Highest rated movies by a specific Gender (M,F)
        4. Highest rated movies by a specific occupation
        5. Quit
        '''
#This function prompts the user to input a file name to open and keeps prompting until a correct name is entered
def open_file(s):
    loop= True
    while loop == True: # here I made a loop so the user will be asked many times until they enter a valid file name
        try:
            promot= input('\nInput {} filename: '.format(s))
            filename= promot
            fp= open(filename,'r',encoding ="windows-1252")# i opened the file in reading mode
            loop = False
        except FileNotFoundError: # I made an except if the file wasn't found an error message wil be printed and the user will be asked again
            print('\nError: No such file; please try again.')
            
    return fp


def read_reviews(N,fp):
    ''' Docstring'''
    reviews= []
    for i in range(N+1):
        user= []
        reviews.append(user)
    for lines in fp:
        line= lines.split("\t")
        tup= (int(line[1]), int(line[2]))
        reviews[int(line[0])].append(tup)
        reviews[int(line[0])].sort()
        
    return reviews
        
    
#This function reads the file using file pointer fp and returns a list of tuples 
def read_users(fp):
    master_list= [[]] # here I made a list within a list as indicated on the pdf
    for lines in fp:
        line= lines.split("|") # this line will split the line and put it into a list witha splited by "|"
        tup= (int(line[1]), line[2], line[3]) # here I added what asked on the pdf into a tuple to add it to the list
        master_list.append(tup)
    
    return master_list
    
#This function reads the file using the file pointer fp 
def read_movies(fp):
    ''' Docstring'''
    movies= [[]] # here I made a list within a list as indicated on the pdf
    for lines in fp: 
        line= lines.split("|") # this line will split the line and put it into a list witha splited by "|"
        genre_for_movie= []
        for index,value in enumerate(GENRES):
            if int(line[int(5 +index)]) ==1:# the pourpose of this line to know if the value is equal to 1, it would add the line to the created list
                genre_for_movie.append(value)
        tup= (line[1],line[2],genre_for_movie) # here I added what asked on the pdf into a tuple to add it to the list
        movies.append(tup)
    return movies
            

#This function reads the movies.txt file using the parameter fp.  and check if       
def year_movies(year,L_movies):
    ''' Docstring'''
    filtered_movies= []
    for index,value in enumerate(L_movies):# the pourpose of this line to enumerate over the file
        if value == []: #the pourpose of this line is to skip the first index because it is an empty list
            continue
        start_index= value[1][7:]
    
        if start_index != "":

            if int(start_index) == int(year): # here I made a comparsion if the the given year equal to the one on the line and if so it would add it to the list
                filtered_movies.append(index)
    filtered_movies.sort()
    return filtered_movies



#This function filters the main movie list to find movies for a specific genre and returns their ids as a list.
def genre_movies(genre,L_movies):
    genre_list = []
    for index,value in enumerate(L_movies): 
        if value == []: #the pourpose of this line is to skip the first index because it is an empty list
            continue
        start_index= value[2]
        if genre.capitalize() in start_index: # here I compared if the genre is the same as the given one
            genre_list.append(index)
        genre_list.sort()
    return genre_list
    
#This function filters the main reviews list to find reviews for a specific gender of users and returns them as a list of lists

def gen_users (gender, L_users, L_reviews):
    ''' Docstring'''
    gen_users= []
    for index,value in enumerate(L_users):
        if value == []: #the pourpose of this line is to skip the first index because it is an empty list
            continue
        start_index= value[1]
        if gender.upper() in start_index: # here I comparsion if the gender is the same as the given one
            gen_users.append(L_reviews[index])
    return gen_users

#This function filters the main reviews list to find records for a specific occupational group of users and returns them as a list of lists of tuples
          
def occ_users (occupation, L_users, L_reviews):
    ''' Docstring'''
    occupation_users= []
    for index,value in enumerate(L_users):
        if value == []: #the pourpose of this line is to skip the first index because it is an empty list
            continue
        start_index= value[2]
        if occupation.upper() in start_index.upper(): # here I comparsion if the occupation is the same as the given one
            occupation_users.append(L_reviews[index])
    return occupation_users
 
#This function calculates the average rating for the reviews in L_reviews list of the movies in L_in list and returns a list of the highest average rated movies and the highest average. Round each average to 2 places
def highest_rated_by_movie(L_in,L_reviews,N_movies):
    master_list = [[]] * (N_movies + 1) # create a list for the number given
    tup_avg = [0] * (N_movies+1) # insialize a value so we won't get an error later
    all_avg = []
    for index in L_in:
        for lists_tup in L_reviews: # compare if the list of tup to the L_reviews
            for tup in lists_tup:
                if index == tup[0]:
                    master_list[tup[0]] = [tup[1]] + master_list[tup[0]] 
    for indx,master_value in enumerate(master_list): 
        if master_value != []:
            
            all_values = 0
            for value in master_value:
                all_values += value
            tup_avg[indx] = float("{:.2f}".format(all_values/len(master_value)))# calculate the avg 
    maximum_avg = max(tup_avg) # calculate the max 
    for ind,avg in enumerate(tup_avg):
        if maximum_avg == avg:# to know the maximum avg
            all_avg.append(int(ind))
    return all_avg,maximum_avg
#This function calculates the average rating for movies by a specific group of users (L_in) and returns a list of the highest average rated movies and the highest average

def highest_rated_by_reviewer(L_in,N_movies):
    master_list = [[]] * (N_movies + 1) # insialize a value so we won't get an error later
    tup_avg = [0] * (N_movies+1) # compare if the list of tup to the L_reviews
    all_avg = []
    for index in L_in:
        for tup in index:
            master_list[tup[0]] = [tup[1]] + master_list[tup[0]] 
    for indx,master_value in enumerate(master_list):
        if master_value != []:
            all_values = 0
            for value in master_value:
                all_values += value
            tup_avg[indx] = float("{:.2f}".format(all_values/len(master_value)))
    maximum_avg = max(tup_avg)
    for ind,avg in enumerate(tup_avg):
        if maximum_avg == avg:# to know the maximum avg
            all_avg.append(int(ind))
    return all_avg,maximum_avg
 #this function would read the files and create the main 3 lists of lists by calling them and Display the menu (MENU) and prompt to choose one of these five different options
def main():
    #open the files
    users_file =open_file("users")
    reviews_file =open_file("reviews")
    movies_file=open_file("movies")
    #read the files
    user_list= read_users(users_file)
    reviews_list= read_reviews(len(user_list),reviews_file)
    movies_list= read_movies(movies_file)

    print(MENU)# print the menu
    loop = True
    while loop != False:
        try:
            promot_for_menu= int(input('\nSelect an option (1-5): '))
            loop = False
        except ValueError:
            print("\nError: not a valid option.")
            # the lines above are writen so if the user enter invalid value it would print an invalid print stement and repromot again
    while promot_for_menu != 5:# if the user enter option 5 it would  quit the loop
        if promot_for_menu == 1: #the menu option 1
            loop = True
            while loop != False:

                try:
                    promot_for_year= int(input('\nInput a year: '))
                    if promot_for_year > 1998 or promot_for_year < 1930: 
                        print("\nError in year.")
                    else:
                        loop = False
                except ValueError:
                    print("\nError in year.")

            call_year_movie = year_movies(int(promot_for_year),movies_list) # calling the function as stated in the pdf
            rated_movie,max_rated_movie= highest_rated_by_movie(call_year_movie,reviews_list,len(movies_list))# calling the function as stated in the pdf
            print('\nAvg max rating for the year is: {}'.format(max_rated_movie)) # printing the average value 
            rated_movie_list= []
            for i in rated_movie:
                rated_movie_list.append(movies_list[i][0])
            print("\n".join(rated_movie_list))
            

        elif promot_for_menu == 2:# menu number 2
            print(f'\nValid Genres are:  {GENRES}') # print the valid Genres
            genre_input= input('Input a genre: ')# ask for a a genre
            loop_genre= False
            while loop_genre == False:
                if genre_input.capitalize() in GENRES:# compare the input to the list of Genres
                    loop_genre = True
                else:
                    print("\nError in genre.")# an invalid print stement if the user enter an invalid genre
                    genre_input= input('Input a genre: ')
            genre_movie= genre_movies(genre_input,movies_list) # calling the function as stated in the pdf
            rated_movie,max_rated_movie= highest_rated_by_movie(genre_movie,reviews_list,len(movies_list)) # calling the function as stated in the pdf
            print('\nAvg max rating for the Genre is: {}'.format(max_rated_movie)) # calculate the Average
            rated_movie_list= []
            for i in rated_movie:
                rated_movie_list.append(movies_list[i][0])
            print("\n".join(rated_movie_list))

            
        elif promot_for_menu == 3: # this will happen if the user enter option 3
            loop = True
            while loop != False:

                
                promot_for_gender= input('\nInput a gender (M,F): ') # promot for an input for gender
                if promot_for_gender.upper() == "M" or promot_for_gender.upper() == "F": # if user enter F or M the function would exit the loop and countinue the code
                    loop = False
                else:
                    print("\nError in gender.")


            call_year_movie = gen_users(promot_for_gender,user_list,reviews_list) # calling the function as stated in the pdf
            rated_movie,max_rated_movie= highest_rated_by_reviewer(call_year_movie,len(movies_list)) # calling the function as stated in the pdf
            print('\nAvg max rating for the Gender is: {}'.format(max_rated_movie))# calculate the Avg
            rated_movie_list= []
            for i in rated_movie:# see if the i value is in rated_movie
                rated_movie_list.append(movies_list[i][0]) # append the value to the list
            print("\n".join(rated_movie_list))
        elif promot_for_menu == 4: # this will happen if the user enter option 4
            print(f'\nValid Occupatipns are:  {OCCUPATIONS}')
            genre_input= input('Input an occupation: ')
            loop_genre= False
            while loop_genre == False:
                if genre_input.lower() in OCCUPATIONS: # to see if the input is in OCCUPATIONS
                    loop_genre = True
                else:
                    print("\nError in occupation.")
                    genre_input= input('Input an occupation: ')
            genre_movie= occ_users(genre_input,user_list,reviews_list) # calling the function as stated in the pdf
            rated_movie,max_rated_movie= highest_rated_by_reviewer(genre_movie,len(movies_list)) # calling the function as stated in the pdf
            print('\nAvg max rating for the occupation is: {}'.format(max_rated_movie)) # calculate the Avg
            rated_movie_list= []
            for i in rated_movie:
                rated_movie_list.append(movies_list[i][0])
            print("\n".join(rated_movie_list))
        else:
            print("\nError: not a valid option.")
        loop = True
        while loop != False:
            try:
                promot_for_menu= int(input('\nSelect an option (1-5): '))
                loop = False
            except ValueError:
                print("\nError: not a valid option.")
    # closing the files
    users_file.close()
    reviews_file.close()   
    movies_file.close()     
    

    pass   # remove this line

if __name__ == "__main__":
    main()
                                           
