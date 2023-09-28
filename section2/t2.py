from sunau import AUDIO_FILE_ENCODING_ADPCM_G721


sum1 = 0
count1 = 0
a = int(input("enter a number: "))

while a != -1:
    sum1 = a + sum1
    count1 = count1 + 1
    a = int(input("enter a number: "))

avg = sum1 / count1
print("avg is ",avg)

