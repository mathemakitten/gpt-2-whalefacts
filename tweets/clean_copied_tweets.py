tweets = []
num_tweets = 0

TWEET_FILE = "copied_whalefact_tweets.txt"  #'/home/rm/jonnysun_tweets/jonny_jan2016_may2017.txt'
OUT_FILE = "whale_tweets.txt"  #'jonny_tweets.txt'

with open(TWEET_FILE, "r") as myfile:
    lines = myfile.readlines()

    for i in range(len(lines)):
        line = lines[i]

        if line[0:6] == 'Reply ':
            num_tweets += 1
            print(num_tweets)
            tweets.append(lines[i-2])

# Write the tweets to a corpus for training

text_corpus = ''

for tweet in tweets:
    text_corpus += tweet
    text_corpus += '\n'

text_corpus += '\n\n'

# Save the data to a file for training
with open(OUT_FILE, "w") as f:
    f.write(text_corpus)


#PYTHONPATH=src ./train.py --dataset /home/rm/gpt2-whalefacts/whale_tweets_all.txt --model_name=345M --val_every 200 --sample_every=250 --learning_rate=0.0001 --run_name='whalefacts'

#PYTHONPATH=src ./train.py --dataset /home/rm/gpt2-whalefacts/jonny_tweets.txt --model_name=345M --val_every 200 --sample_every=250 --learning_rate=0.0001 --run_name='jonny_test'