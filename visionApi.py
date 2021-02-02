#visionをインポート
from google.cloud import vision

#イメージを開いて読み込む
with open('./photo.jpg','rb') as image_file:
  content = image_file.read()

image = vision.Image(content=content)

#インスタンスの生成
annotator_client = vision.ImageAnnotatorClient()

response_data = annotator_client.label_detection(image=image)

labels = response_data.label_annotations

print('--result--')
for label in labels:
  print(label.description,':', round(label.score * 100,2),'%')
print('--result--')




