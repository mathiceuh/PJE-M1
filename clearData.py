import re
import csv

emoji_pos = ["😁", "😍", "😄", "🙂"]
emoji_neg = ["🤮", "🤬", "🙁", "☹️", "😡", "😠", "😤", "😢", "😭"]


def clean_text(text):
    # Supprimer les mentions, hashtags, RT et liens
    text = re.sub(r"(@[\w]+)", "", text)
    text = re.sub(r"(#[\w]+)", "", text)
    text = re.sub(r"RT", "", text)
    text = re.sub(r"https?://\S+", "", text)

    # Supprimer les emojis
    for c in text:
        if c in emoji_pos or c in emoji_neg:
            text = text.replace(c, "")

    return text.strip()


def clean_double(tweets):
    temp = []
    unique_tweets = []
    for tweet in tweets:
        if tweet[1] not in temp:  # On considère que l'ID est en position 1
            temp.append(tweet[1])
            unique_tweets.append(tweet)
    return unique_tweets


most_used_english_words = ["the", "of", "and", "is", "was", "it", "I", "he"]


def clean_english_tweets(tweets):
    not_english_tweets = []
    for tweet in tweets:
        words = tweet[5].split(" ")  # Le texte du tweet est en position 5
        find = False
        for word in words:
            if word.lower() in most_used_english_words:
                find = True
                break
        if not find:
            not_english_tweets.append(tweet)
    return not_english_tweets


input_file = "tweetpje.csv"

tweets_test = []

# Lecture du fichier CSV
with open(input_file, newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    # Si ton CSV a un entête, la sauter
    next(reader, None)
    for row in reader:
        # Chaque ligne devient un tweet
        # Vérifie que le CSV a exactement 6 colonnes comme ton exemple
        if len(row) >= 6:
            tweets_test.append(row[:6])


# Nettoyage
cleaned_tweets = clean_double(tweets_test)
cleaned_tweets = clean_english_tweets(cleaned_tweets)
cleaned_tweets = [
    [clean_text(elt) for elt in tweet]
    for tweet in cleaned_tweets
]

# Écriture dans un CSV
with open("nettoye.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    # Éventuellement écrire l'entête
    writer.writerow(["Col1", "ID", "Date", "Produit", "Utilisateur", "Texte"])
    # Écrire les lignes nettoyées
    writer.writerows(cleaned_tweets)

print("Fichier 'nettoye.csv' créé avec succès !")
