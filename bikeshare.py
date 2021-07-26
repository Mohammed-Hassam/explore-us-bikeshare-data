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

    print('Enter The City Name [ Available cities : chicago , new york city  , washington]: ')
    city = input()
    cities = ['chicago','new york city','washington']
    while city == '':
        print('please enter the corrcet city Name')
        city = input()
    while city != '':
        if city in cities:
            print("Enter The Month['all if no filter','january', 'february', 'march', 'april', 'may', 'june'] :")
            break
        else:
            print('Please Enter The Corrcet City Name')
            city = input()
    # TO DO: get user input for month (all, january, february, ... , june)
    month= input()
    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    while month == '':
        print('please enter the corrcet month')
        month= input()
    while month != '':
        if month in months :
            print(' Please Enter the day:[ sunday , monday , tuesday , ..... ] ')
            break
        else:
            print('please enter the corrcet month')
            month= input()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input()
    days =['all','sunday', 'monday', 'tuesday', 'wednesday','thursday','friday','saturday']
    while day == '':
        print('please enter the corrcet day')
        day= input()
    while day != '':
        if day in days :
            break
        else:
            print('please enter the corrcet day')
            day= input()

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    m_c_m =df["month"].mode()[0]
    print('the most common month is :' , m_c_m  )
    # TO DO: display the most common day of week
    m_c_d =df["day_of_week"].mode()[0]
    print('the most common day is :' , m_c_d  )
    # TO DO: display the most common start hour
    m_c_h =df["hour"].mode()[0]
    print('the most common hour is :' , m_c_h  )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    c_s_s = df["Start Station"].mode()[0]
    print("the most popular comonly use start station is : " , c_s_s)
    # TO DO: display most commonly used end station
    c_e_s = df["End Station"].mode()[0]
    print("the most popular comonly use End station is : " , c_e_s)
    # TO DO: display most frequent combination of start station and end station trip
    combination_of_start_station_and_end_station_trip =  df.groupby(['Start Station','End Station']).size().idxmax()
    print( " most frequent  trip",combination_of_start_station_and_end_station_trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('The total travel time :' , total_time)

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('The average travel time :' , mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("counts of User Type" )
    print( df['User Type'].str.count('Customer').sum(),"Customer")
    print( df["User Type"].str.count("Subscriber").sum() , "Subscriber")

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print( "counts of Male " ,  df['Gender'].str.count('Male').sum())
        print( "counts of Female " ,  df["Gender"].str.count("Female").sum())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print( "earliest birthday " ,df["Birth Year"].min())
        print( "most recent birthday " , df["Birth Year"].max())
        print( "most common birthday " , df["Birth Year"].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
