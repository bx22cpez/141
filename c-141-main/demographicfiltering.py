import numpy as numpy
import pandas as pd

with open("articles.csv") as f:
    reader=csv.reader(f)
    data=list(reader)
    all_movies=data[1:]
    