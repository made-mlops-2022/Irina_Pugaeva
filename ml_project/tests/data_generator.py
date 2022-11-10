import pandas as pd
import scipy.stats as stats
from faker import Faker

faker = Faker()
SIZE = 100

def generate_fake_normal_data(size):
    rows = {'age': stats.norm(loc=54.54, scale=9.05).rvs(size),         
             'trestbps': stats.norm(loc=131.70, scale=17.76).rvs(size),
             'chol': stats.norm(loc=247.35, scale=52).rvs(size),
             'thalach': stats.norm(loc=150, scale=23).rvs(size)}
    fake_normal_data = pd.DataFrame(rows)
    return fake_normal_data

def generate_fake_not_normal_data(size):
    rows = [{'sex': faker.pyint(0, 1),
             'cp': faker.pyint(0, 3),
             'fbs': faker.pyint(0, 1),
             'restecg': faker.pyint(0, 2),
             'exang': faker.pyint(0, 1),
             'oldpeak': faker.pydecimal(0, 7),
             'slope': faker.pyint(0, 2),
             'ca': faker.pyint(0, 3),
             'thal': faker.pyint(0, 2),
             'condition': faker.pyint(0, 1)} for x in range(size)]
    fake_not_normal_data = pd.DataFrame(rows)
    fake_not_normal_data['oldpeak'] = fake_not_normal_data['oldpeak'].astype('float64')
    return fake_not_normal_data

def generate_fake_dataset(size=SIZE):
    return pd.concat([generate_fake_normal_data(size), generate_fake_not_normal_data(size)], axis=1)
