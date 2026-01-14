# importing the required libraries
import numpy as np
from imgbeddings import imgbeddings
from PIL import Image
import psycopg2
import os

# connecting to the database - replace the SERVICE URI with the service URI
conn = psycopg2.connect("<SERVICE_URI>")

for filename in os.listdir("stored-faces"):
    # opening the image
    img = Image.open("stored-faces/" + filename)
    # loading the `imgbeddings`
    ibed = imgbeddings()
    # calculating the embeddings
    embedding = ibed.to_embeddings(img)
    cur = conn.cursor()
    cur.execute("INSERT INTO pictures values (%s,%s)", (filename, embedding[0].tolist()))
    print(filename)
conn.commit()


# loading the face image path into file_name variable
file_name = "C:\Users\sasha\OneDrive\Bureau\usechat\felix le beaugarcon.png"  # replace <INSERT YOUR FACE FILE NAME> with the path to your image
# opening the image
img = Image.open(file_name)
# loading the `imgbeddings`
ibed = imgbeddings()
# calculating the embeddings
embedding = ibed.to_embeddings(img)