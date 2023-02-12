# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
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
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city=input('Would you like to see data for Chicago, New York city, or Washington?')
    while city.lower() not in ['chicago', 'new york city','washington' ]:
        city=input('Would you like to see data for Chicago, New York, or Washington?' )
    city=city.lower()
  


    # get user input for month (all, january, february, ... , june)
    
    month=input(' Which month - all January, February, March, April, May, or June?')
    while month.lower() not in ['all', 'january','february', 'march', 'april', 'may','june']:
        month=input('Which month - all January, February, March, April, May, or June?')
    month=month.lower()


    # get user input for day of week (all, monday, tuesday, ... sunday)

    day=input('Which day - all,Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?')
    while day.lower() not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']:
        day=input('Which day - all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?')
    day=day.lower()


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
    df = pd.read_csv(CITY_DATA[city])   #in file (read_csv) change it to (dataframe)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name() # in file (weekday_name)

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
def time_statss(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'], errors='coerce')

    # display the most common month
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    common_month=df['month'].mode()[0]
    print('Most common month :',common_month)


    # display the most common day of week
    df['day'] = pd.DatetimeIndex(df['Start Time']).day
    common_day=df['day'].mode()[0]
    print('Most common day of week',common_day)


    # display the most common start hour
    df['hour'] = pd.DatetimeIndex(df['Start Time']).hour
    common_hour=df['hour'].mode()[0]
    print('Most common start hour',common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station=df['Start Station'].mode()[0]
    print('most commonly used start station is ',start_station)


    # display most commonly used end station
    end_station=df['End Station'].mode()[0]
    print('most commonly used end station is ',end_station)


    # display most frequent combination of start station and end station trip
    print(df.groupby(['Start Station','End Station']).size().sort_values(ascending=False).index[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)   
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['Trip Duration'].sum()


    # display mean travel time
    df['Trip Duration'].mean()


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts().to_string()
    print('counts of user types',user_types)


    # Display counts of gender
    try:
        gender = df['Gender'].value_counts().to_string()
        print('counts gender ',gender)
        
    except:
        print('no gender information')
    try:
        print('earliest year of birth', df['Birth Year'].min())
        print('recent year of birth', df['Birth Year'].max())
        print('Most common year of birth' ,df['Birth Year'].mode()[0])
           # or Birth_Year = df['Birth Year'].value_counts().index[0]
    except:
        print("no birth information")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_statss(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        x=0
        y=5
        while True:
            display_data=input('would you like to see some data ?')
            print(df[x:y])
            x+=5
            y+=5
            if display_data.lower() != 'yes':
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
    main()
   