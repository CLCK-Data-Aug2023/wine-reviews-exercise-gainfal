import pandas as pd
reviews = pd.read_csv("data/winemag-data-130k-v2.csv")
reviews_per_country = reviews.country.value_counts()
country_mean_ratings = reviews.groupby('country').points.mean()
reviews_df =  pd.DataFrame({
                            "count":reviews_per_country,
                             "points":round(country_mean_ratings,1)})
reviews_sort_df=reviews_df.sort_values(by='count',ascending=False)
reviews_sort_df.to_csv("data/reviews-per-country.csv",index=True)


