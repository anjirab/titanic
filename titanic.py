import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
titanic = pd.read_csv('titanic.csv')
titanic.head()
plt.plot(titanic["age"])
plt.show()