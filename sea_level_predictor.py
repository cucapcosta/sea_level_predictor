import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # Create scatter plot
    fig = plt.figure(figsize=(12,6))
    plt.scatter(x='Year', y='CSIRO Adjusted Sea Level', data=df)

    # Create first line of best fit
    slope, y_intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    #print("Ponto 1:", slope)
    new_years = np.arange(1880, 2051)
    sea_new_years = y_intercept + slope * new_years
    print('P1:', sea_new_years)
    plt.plot(new_years, sea_new_years, label='First line of best fit', color='red')

    # Create second line of best fit
    slope, y_intercept, r_value, p_value, std_err = linregress(df[df["Year"] > 1999]['Year'], df[df['Year'] > 1999]['CSIRO Adjusted Sea Level'])
    #print('Ponto 2:', slope)
    new_years = np.arange(2000, 2051)
    sea_new_years = y_intercept + slope * new_years
    print('P2:', sea_new_years)
    plt.plot(new_years, sea_new_years, label='Second line of best fit', color='green')



    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()