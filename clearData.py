import re

emoji_pos = ["😁","😍","😄","🙂"]
emoji_neg = ["🤮","🤬","🙁","☹️","😡","😠","😤","😢","😭"]

def clean_tweet(tweet):
    tweet = re.sub(r"(@[\w]+)","",tweet)        # Supprimer les mentions @
    tweet = re.sub(r"(#[\w]+)","",tweet)        # Supprimer les #
    tweet = re.sub(r"RT","",tweet)              # Supprimer les RT.
    tweet = re.sub(r"https?://\S+","",tweet)    # Supprimer les liens http et https et ce qui les succédent.
    for c in tweet:
        if c in emoji_pos or c in emoji_neg:
            tweet = tweet.replace(c, "")
    tweet = tweet.strip()
    return tweet

tt = "@richardebaker no 😡. it is too big. I'm quite happy with the Kindle2. #badthing"
print(tt)
print(clean_tweet(tt))
        
# enlever les @, #, RT, URL et lʼURL associée
# retirer les émoticones (positifs et négatives)
# enlever les doublons (basé sur les id dans un premier temps)
# Vérifier que la plupart des tweets sont français (algo de calcul du nombre de lettre et analyse pour déterminer la langue)