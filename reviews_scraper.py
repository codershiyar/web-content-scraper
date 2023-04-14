import requests
from bs4 import BeautifulSoup
import json
import csv
import time

# decathlon scraper reviews
total_per_page = "200";
urls =[
"https://www.decathlon.nl/nl/ajax/nfs/reviews/8370292,8397290,8502284?count="+total_per_page,
"https://www.decathlon.nl/nl/ajax/nfs/reviews/8510103,8510106?count="+total_per_page,
"https://www.decathlon.nl/nl/ajax/nfs/reviews/8580219,8608672?count="+total_per_page,
"https://www.decathlon.nl/nl/ajax/nfs/reviews/8641926,8641924,8641929,8641931,8641932,8641933?count="+total_per_page,
 "https://www.decathlon.nl/nl/ajax/nfs/reviews/8560941,8650772,8506622,8600783?count="+total_per_page,
"https://www.decathlon.nl/nl/ajax/nfs/reviews/8491498,8491500,8548323,8616325,8616377,8678296,8774090?count="+total_per_page,
"https://www.decathlon.nl/nl/ajax/nfs/reviews/8642450,8544452,8758322,8758324?count="+total_per_page,
"https://www.decathlon.nl/nl/ajax/nfs/reviews/8545301?count="+total_per_page,
"https://www.decathlon.nl/nl/ajax/nfs/reviews/8545301?count="+total_per_page,
"https://www.decathlon.nl/nl/ajax/nfs/reviews/8640301,8754004,8640296,8640297,8641502,8641503,8738716?count="+total_per_page,
"https://www.decathlon.nl/nl/ajax/nfs/reviews/8545278?count="+total_per_page
]


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

total_reviews = 0
total_words = 0
reviews_over_100_words = 0

with open('decathlon.csv', 'w', newline='') as csvfile:
    fieldnames = ['publishedAt', 'title', 'body', 'rating', 'author', 'useful']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

for url in urls:
    for i in range(15):
        try:
            reviews_url = url + "&page="+ str(i+1)
            print(reviews_url)
            response = requests.get(reviews_url, headers=headers)
            response_as_json = json.loads(response.content)
            reviews = response_as_json["reviews"]
            for review in reviews:
                publishedAt = review['review']['publishedAt']
                title = review['review']['title']
                body = review['review']['body']
                rating = review['review']['rating']
                author = ""
                try:
                    author = review['author']
                except:
                    print("This review has no author identified.")
                useful =  review['review']['useful']
                
                # Update the total number of reviews
                total_reviews += 1
                
                # Update the total number of words in reviews
                total_words += len(body.split())
                
                # Update the number of reviews that have more than 100 words
                if len(body.split()) > 100:
                    reviews_over_100_words += 1
                
                with open('decathlon.csv', 'a', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    # if  author["countryLabel"] == 'Nederland':
                    writer.writerow({'publishedAt': publishedAt, 'title': title, 'rating': rating, 'author':author, 'useful': useful})
            print("Link: " + reviews_url +" is done")
            time.sleep(1.5)
        except:
            print("")
    
# Calculate the average number of words per review
average_words_per_review = total_words / total_reviews

# Calculate the percentage of reviews that have more than 100 words
percent_reviews_over_100_words = (reviews_over_100_words / total_reviews) * 100

# Print the results
print("Total reviews: ", total_reviews)
print("Average number of words per review: ", int(average_words_per_review))

print("Percentage of reviews with more than 100 words: ", "{:.2f}".format(round(percent_reviews_over_100_words, 2) ), "%")
print("Done")