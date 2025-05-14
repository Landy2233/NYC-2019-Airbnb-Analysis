# NYC 2019 Airbnb Analysis

This project involves the analysis and visualization of Airbnb data for New York City in 2019. It uses the **AB_NYC_2019** dataset to explore key aspects such as room pricing, location distribution, and availability of Airbnb listings in the city.

## Table of Contents
- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Data](#data)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project aims to provide insights into the Airbnb market in New York City by exploring data such as:
- The distribution of listings by neighborhood
- Price analysis by room type and neighborhood
- Availability analysis throughout the year
- Interactive visualizations using Dash and Plotly

## Technologies Used

- **Python**: The main programming language.
- **Pandas**: Data cleaning and manipulation.
- **Dash**: Web framework for creating interactive visualizations and dashboards.
- **Plotly**: Visualization library for creating dynamic charts and graphs.
- **CSV (Comma-Separated Values)**: Data format for storing the Airbnb dataset.
  
## Data

The dataset used in this project is the **AB_NYC_2019.csv** dataset, which contains information about Airbnb listings in New York City in 2019. The data includes details such as:
- Listing ID
- Host name
- Neighborhood group (Borough)
- Room type
- Price
- Minimum nights
- Availability

### Data Cleaning

Data cleaning steps include:
- Removing listings with invalid price or minimum night values.
- Handling missing data and outliers.
- Converting the price column to numeric for better analysis.

The cleaned data has been saved in the `cleaned_airbnb_data.csv` file.

## Installation

To run this project locally, follow these steps:

### Prerequisites:
Make sure you have **Python 3.x** installed. You also need the following libraries:
- `pandas`
- `dash`
- `plotly`

### Steps to Install:
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/NYC-2019-Airbnb-Analysis.git
