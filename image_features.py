import pandas as pd

face_features = pd.read_csv("C:\\Users\\Manas\\PROJECTS\\ML project\\img_align_celeba\\attributes\\face_features.csv")

x = 1
for image in face_features['features']:
  f = open("C:\\Users\\Manas\\PROJECTS\\ML project\\img_align_celeba\\attributes\\text_features\\" + str(x) + ".txt", "w")
  f.write(image)
  f.close()
  print("Uploaded for image: ", x)
  x = x+1