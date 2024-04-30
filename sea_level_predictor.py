import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    ax.set_xlabel('Year')
    ax.set_ylabel('CSIRO Adjusted Sea Level')

    # Create first line of best fit
    future_years = np.arange(1880, 2051)
    reg = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(future_years, reg.intercept + reg.slope * future_years)

    # Create second line of best fit
    filtered = df[df['Year'] >= 2000]
    starts_2000 = np.arange(2000, 2051)
    res = linregress(filtered['Year'], filtered['CSIRO Adjusted Sea Level'])
    ax.plot(starts_2000, res.intercept + res.slope * starts_2000)

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()