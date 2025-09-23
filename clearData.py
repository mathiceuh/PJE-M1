import re

emoji_pos = ["😁","😍","😄","🙂"]
emoji_neg = ["🤮","🤬","🙁","☹️","😡","😠","😤","😢","😭"]

def clean_text(text):
    # Sur la base d'expressions régulières :
    text = re.sub(r"(@[\w]+)","",text)        # Supprimer les mentions @
    text = re.sub(r"(#[\w]+)","",text)        # Supprimer les #
    text = re.sub(r"RT","",text)              # Supprimer les RT.
    text = re.sub(r"https?://\S+","",text)    # Supprimer les liens http et https et ce qui les succédent.
    for c in text:
        if c in emoji_pos or c in emoji_neg:
            text = text.replace(c, "")
    text = text.strip()
    return text

def clean_double(tweets):
    temp = []   # tab temporaire pour stocker les id lus.
    unique_tweets = []
    for tweet in tweets:
        if tweet[1] not in temp: # Si on admet que les identifiants de tweet sont toujours en 2e position.
            temp.append(tweet[1])  
            unique_tweets.append(tweet)
    return unique_tweets

# Pour limiter le nombre de tweets Anglais sans utiliser de bibliothèque, 
# on peut se baser sur quelques mots les plus couramment utilisé dans cette langue.
# Et ainsi filtrer les phrases par rapport à ceux-ci.

most_used_english_words = ["the","of","and","is","was","it","I","he"]

def clean_english_tweets(tweets):
    not_english_tweets = []
    for tweet in tweets:
        words = tweet[5].split(" ") # Si on admet que les messages de tweet sont toujours en 6e position.
        find = False
        for word in words:
            if word in most_used_english_words:
                find = True
        if not find:
            not_english_tweets.append(tweet)
    return not_english_tweets

tweets_test = [
    ["4","3","Mon May 11 03:17:40 UTC 2009","kindle2","tpryan","@stellargirl I loooooooovvvvvveee my Kindle2. Not that the DX is cool, but the 2 is fantastic in its own right."],
    ["4","3","Mon May 11 03:18:03 UTC 2009","kindle2","vcu451","Reading my kindle2...  Love it... Lee childs is good read."],
    ["4","5","Mon May 11 03:18:54 UTC 2009","kindle2","chadfu","Ok, first assesment of the #kindle2 ...it fucking rocks!!!"],
    ["4","6","Mon May 11 03:19:00 UTC 2009","kindle2","mark","Ok, c'est vraiment cool !"],
    ["0","10","Mon May 11 05:19:00 UTC 2009","kindle2","johndoe","No 😡, c'est trop grand, c'était mieux avec #kindle2."]
]

cleaned_tweets = []
cleaned_tweets = clean_double(tweets_test)
cleaned_tweets = clean_english_tweets(cleaned_tweets)
cleaned_tweets = [
    [clean_text(elt) for elt in tweet]
    for tweet in cleaned_tweets
]
print(cleaned_tweets)

# Vérifier que la plupart des tweets sont français (algo de calcul du nombre de lettre et analyse pour déterminer la langue)