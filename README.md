# Simpson Analysis: IMBD Score Prediction App  
---

This repo contains my analysis of Simpsons episode and script data from the first 26 seasons of the show. The Simpsons episode database is from [this Kaggle competition](https://www.kaggle.com/wcukierski/the-simpsons-by-the-data). I created a local PostgreSQL database using this data and then accessed it through a [Jupyter Notebook](Simpsons_IMBD_Prediction_Modeling.ipynb). The Notebook shows my querying, cleaning, and manipulation of the data to obtain my model features as well all the sklearn models I tried using to predict low, medium or high IMBD score.

My best and final model was a random forest classifier which I then used to create a prediction app. The app allows users to see how changing one variable affects the prediction while holding other values constant. Download all files and run ```python simpsons_imbd_predictor_app.py``` to load the app in your local browser.

Check out [my blog](https://lauraehoward.weebly.com/blog/the-good-the-bad-and-the-meh-classifying-the-simpsons-episode-quality) on this project if you're interested in learning more!

<p align="center">
  <img static/app_screenshot.png />
</p>
