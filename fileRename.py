import os

files = os.listdir("clutteredFolder")
i = 1
for file in files:
    if file.endswith(".jpg"):
        print(file)
        os.rename(f"clutteredFolder/{file}", f"clutteredFolder/{i}.jpg")
        i = i + 1
        print(file)