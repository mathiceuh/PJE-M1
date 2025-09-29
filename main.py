import re
import csv
import streamlit as sl

sl.title("Premier pas - StreamLit")
sl.write("Ceci est un premier site web généré avec StreamLit.")

val = sl.number_input("Entrer un nombre :")
if val:
    sl.success(val)

    with open('tweets.csv', 'r', encoding="utf-8") as file, \
            open('tweets_cleaned.csv', 'w', newline='', encoding="utf-8") as file_out:
        reader = csv.reader(file, delimiter=",")
        writer = csv.writer(file_out, delimiter=',')
    for row in reader:
        # GERER LES DOUBLONS

        # tweet_id = row[1]
        # if tweet_id not in id_connus:
        #     id_connus.append(tweet_id)
        #     unique_tweet.append(row)
        newline = []
        for elt in unique_tweet:
            print(elt)
            elt = re.sub(r"(@[\w]+)","",elt)        # Supprimer les mentions @
            elt = re.sub(r"(#[\w]+)","",elt)        # Supprimer les #
            elt = re.sub(r"RT","",elt)              # Supprimer les RT.
            elt = re.sub(r"https?://\S+","",elt)    # Supprimer les liens http et https et ce qui les succédent.
            for c in elt:
                if c in emoji_pos or c in emoji_neg:
                    elt = elt.replace(c, "")
            # print(elt)
            newline.append(elt)
        writer.writerow(newline)

print("OK")
        
# ELEMENTS VISUELS :
# Proportion de tweets négatif, neutre et positif.

# FONCTIONNALITES :
# Ajouter un bouton pour analyser des tweets.