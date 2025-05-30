import pandas as pd

from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib

from preprocessing import clean_dataset


paris_apartments_dataset = pd.read_csv("../scraping/seloger_scraper/seloger_scraper/apartments_paris.csv")

paris_apartments_dataset_cleaned = clean_dataset(paris_apartments_dataset)

encoder = LabelEncoder()
paris_apartments_dataset_cleaned["zipCode"] = encoder.fit_transform(paris_apartments_dataset_cleaned["zipCode"])

scaler = StandardScaler()
paris_apartments_dataset_cleaned[["numberOfRooms", "numberOfBedrooms", "livingSpace", "apartmentFloor", "price"]] = scaler.fit_transform(paris_apartments_dataset_cleaned[["numberOfRooms", "numberOfBedrooms", "livingSpace", "apartmentFloor", "price"]])

X_train, X_test, y_train, y_test = train_test_split(paris_apartments_dataset_cleaned[["numberOfRooms", "numberOfBedrooms", "livingSpace", "apartmentFloor", "zipCode"]], paris_apartments_dataset_cleaned["price"], test_size=0.15, random_state=20190511)
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

y_pred = linear_model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)


joblib.dump(linear_model, 'linear_regression_apartments_paris.pkl')
#joblib.dump(best_model, 'best_model.pkl')





