import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

spring = pd.read_table("C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/spring_skin.txt", sep=',', names=['R','G','B'])
summer = pd.read_table("C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/summer_skin.txt", sep=',', names=['R','G','B'])
fall = pd.read_table("C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/fall_skin.txt", sep=',', names=['R','G','B'])
winter = pd.read_table("C:/Users/sophi/OneDrive/바탕 화면/Folder/인공지능/Skin color detection/winter_skin.txt", sep=',', names=['R','G','B'])

spring['color'] = 'spring'
summer['color'] = 'summer'
fall['color'] = 'fall'
winter['color'] = 'winter'

df = pd.concat([spring,summer,fall,winter])
data = df[['R','G','B']]
label = df['color']

train_data, test_data, train_label, test_label = train_test_split(data, label, random_state=50)

knn = KNeighborsClassifier(n_neighbors=3, weights='distance')
knn.fit(train_data, train_label)
print(knn.score(test_data, test_label))
print(knn.predict([[228, 187, 168]]))