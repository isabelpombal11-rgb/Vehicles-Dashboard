# Vehicles Dashboard: US Used Car Listings

An interactive web app for exploring more than 51,000 used car advertisements in the United States, built with Streamlit and Plotly and deployed on Render.

**Live app:** https://vehicles-dashboard-b89w.onrender.com

> The app runs on Render's free tier and sleeps after a period of inactivity, so the first visit may take about a minute to load. The app interface is in Portuguese.

## About the project

This project was built as part of the TripleTen Data Analytics program (Sprint 5, Software Development Tools). The goal was to take a dataset from exploratory analysis in a Jupyter notebook all the way to a publicly accessible web application, using the tools of a real development workflow: virtual environments, Git and GitHub, and cloud deployment.

## What the app does

The dashboard generates two interactive Plotly charts on demand: a histogram showing the distribution of vehicle mileage (`odometer`), and a scatter plot of mileage against asking price (`price`) to explore how usage affects value. Each chart is created by clicking its corresponding button.

## Dataset

`vehicles_us.csv` contains 51,525 listings with 13 columns covering vehicle characteristics (model, model year, cylinders, fuel, transmission, type, paint color, 4WD), condition, and listing details (price, date posted, days listed).

## Key findings

The full exploratory analysis is in [`notebooks/EDA.ipynb`](notebooks/EDA.ipynb).

**The market is dominated by well-used vehicles.** The median model year is 2011 and median mileage is around 113,000 miles. Prices are strongly right-skewed, with a median of $9,000 but a mean of $12,132, pulled up by a small number of high-end listings reaching $375,000.

**Price falls as mileage rises, and depreciation is steepest early on.** The drop is sharpest over the first 200,000 miles and then levels off. The isolated high-priced points are luxury vehicles, where price depends more on make and model than on usage.

**Supply is concentrated in good-condition SUVs, trucks, pickups and sedans.** Most listings are described as "excellent" or "good", and these vehicle types make up the bulk of supply in every condition category.

**The data needs cleaning before any modeling.** Around 15% of listings have no mileage recorded, the minimum price is $1 (a placeholder rather than a real asking price), and missing values in `is_4wd` most likely mean the vehicle is not 4WD rather than that the information is unknown.

## Tech stack

Python, pandas, Plotly Express, Streamlit, Git/GitHub, Render.

## Project structure

```
Vehicles-Dashboard/
├── app.py                  # Streamlit application
├── vehicles_us.csv         # Dataset
├── requirements.txt        # Dependencies
├── notebooks/
│   └── EDA.ipynb           # Exploratory data analysis
└── .streamlit/
    └── config.toml         # Server configuration for deployment
```

## Running locally

```bash
git clone https://github.com/isabelpombal11-rgb/Vehicles-Dashboard.git
cd Vehicles-Dashboard
python -m venv vehicles_env
source vehicles_env/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Then open the local address shown in the terminal.

## Author

**Isabel Pombal**, petroleum engineer with 13+ years of experience in the oil and gas industry, now working in data analytics.

[LinkedIn](www.linkedin.com/in/isabel-mazingo-de-pombal-43a98a48)

