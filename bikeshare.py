import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    while True:
      city = input("Please choose one of these cities?, chicago, new york city, washington").lower()
      if city not in ['new york city', 'chicago', 'washington']:
        print("Please, Try again.").lower()
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
      month = input("Please choose one month for analysis?, january, february, march, april, may, june, or all").lower()
      if month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        print("Please, Try again.").lower()
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
      day = input("Which day you would like to analyze?, sunday, monday, tuesday, wednesday, thursday, friday, satday, or type all").lower()
      if day not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']:
        print("Please, Try again.").lower()
        continue
      else:
        break

    print('-'*40)
    return city, month, day
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    popular_month = df['month'].mode()[0]
    print('The most frequent month is:', popular_month)
    
        
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most frequent day of the week is:', popular_day)
    
        
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    
    popular_hour = df['hour'].mode()[0]
    print('The most frequent Hour is:', popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    try:
        Start_Station = df['Start Station'].value_counts().idxmax()
        print('The most popular start Station is:', Start_Station)
    except: KeyError

    # TO DO: display most commonly used end station
    try:
        End_Station = df['End Station'].value_counts().idxmax()
        print('The most popular End Station is:', End_Station)
    except: KeyError
        
    # TO DO: display most frequent combination of start station and end station trip
    try:
        Combination_Station = df.groupby(['Start Station', 'End Station']).count()
        print('The most popular combination of start and end Station is:', Start_Station, End_Station)
    except: KeyError
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_travel_time = df['Trip Duration'].sum()
    print('The Total Travel time is:', Total_travel_time)

    # TO DO: display mean travel time
    Mean_travel_time = df['Trip Duration'].mean()
    print('The Mean Travel time is:', Mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    user_gender = df['Gender'].value_counts()
    print(user_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    
    earliest=int(df['Birth Year'].min())
    print("The Earliest year of birth", earliest)
    most_recent=int(df['Birth Year'].max())
    print("The most recent year of birth", most_recent)
    common=int(df['Birth Year'].mode()[0])
    print("The Earliest year of birth", common)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    keep_asking = True
    while (keep_asking):
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        if view_display == "no": 
            keep_asking = False



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main() 
