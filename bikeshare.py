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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input('Please insert the city you want to analyze (Chicago, New York City, Washington): ').lower()
        if city in CITY_DATA.keys():
            print('Analyze data for ' + city.title())
            break
        else:
            print('The input is not valid.')
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please insert the month you want to analzye (January to June). Type in "All" for all six months: ').title()
        if month in ('January', 'February', 'March', 'April', 'May', 'June'):
            print('Analyze data for ' + month)
            break
        elif month == 'All':
            print('Analyze data for all available months')
            break
        else:
            print('The input is not valid.')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please insert the weekday you want to analzye (Monday to Sunday). Type in "All" for all weekdays: ').title()
        if day in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'):
            print('Analyze data for ' + day)
            break
        elif day == 'All':
            print('Analyze data for all days.')
            break
        else:
            print('The input is not valid.')

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
    
    df = pd.read_csv(city.replace(" ", "_").lower() + '.csv')

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['weekday'] = df['Start Time'].dt.day_name()
    
    if month != 'All':
        df = df[df['month'] == month]
        
    if day != 'All':
        df = df[df['weekday'] == day]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print(df.head())
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is {}.'.format(common_month))


    # TO DO: display the most common day of week
    common_weekday = df['weekday'].mode()[0]
    print('The most common day of week is {}.'.format(common_weekday))


    # TO DO: display the most common start hour
    common_starthour = df['Start Time'].dt.hour.mode()[0]
    print('The most common start hour is {}.'.format(common_starthour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most common start station is {}.'.format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most common end station is {}.'.format(common_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    startend = 'from ' + df['Start Station'] + ' to ' + df['End Station']
    common_startend = startend.mode()[0]
    print('The most common combination of start station and end station is {}.'.format(common_startend))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('The total travel time is {}.'.format(total_travel))


    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('The average travel time is {}.'.format(mean_travel))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types')
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    print('Counts of gender')
    print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_birth = int(df['Birth Year'].min())
    most_recent_birth = int(df['Birth Year'].max())
    most_common_birth = int(df['Birth Year'].mode())
    print('The earliest year of birth is {}, the most recent is {} and the most common is {}.'.format(earliest_birth, most_recent_birth, most_common_birth))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Displays raw data on bikeshare users."""
    while True:
        rawdata = input('Do you want to see 5 lines of raw data? (yes/no): ')

        if rawdata == 'no':
            break
        elif rawdata == 'yes':
            print(df.head())
        else:
            print('This was not a valid input')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
