import requests,csv,time


url = "https://api.spectrumcustomizer.com/api/badwords/has-any/"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Origin":"https://xboxdesignlab.xbox.com",
    "Content-Type":"application/json",
    "Host":"api.spectrumcustomizer.com",
}

words = open("E:\\dictionary.txt",'r')

try:
    with open("./banned_words.csv",'w+') as f:
        csvwriter = csv.writer(f,lineterminator="\n")
        csvwriter.writerow(["word","banned"])
        for line in words:
            stipped = line.strip()
            data = {
                "clientHandle":"xbox",
                "phrase":stipped
            }
            
            r = requests.post(url,json=data)
            print(stipped,r.text)
            csvwriter.writerow([stipped,r.text.strip()])
except Exception as e:
    pass        
finally:
    words.close()
