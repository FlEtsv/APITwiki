import asyncio
import time

from twikit import Client, TooManyRequests

USERNAME = 'USUARIO'
EMAIL = 'EMAIL'
PASSWORD = 'CONTRASEÑA'

#iniatilize the client
client = Client('en-US')

"""
obtener la totalidade de los tweets de un usuario
"""
async def getTweet():
    await client.login(auth_info_1=USERNAME, auth_info_2=EMAIL, password=PASSWORD)
    screen_name = 'elonmusk'
    user = await client.get_user_by_screen_name(screen_name)
    user_id = user.id
    seen_tweet_ids = []  # Initialize the list of seen tweet IDs
    cursor = None  # Initialize the cursor for pagination
    all_tweets = []  # Initialize a list to store all tweets

    while True:
        try:
            result = await client.get_user_tweets(user_id, 'Tweets', count=20, cursor=cursor)
            if not result:  # Si no hay tweets, rompe el bucle
                print("No more tweets available.")
                break
            tweets = [tweet for tweet in result if tweet.id not in seen_tweet_ids]
            if not tweets:  # Si no hay nuevos tweets, rompe el bucle
                print("No new tweets found.")
                break
            all_tweets.extend(tweets)
            seen_tweet_ids.extend([tweet.id for tweet in tweets])
            cursor = result.next_cursor
            if not cursor:  # Si no hay siguiente cursor, rompe el bucle
                print("Reached the end of tweets.")
                break
        except TooManyRequests as e:
            if e.rate_limit_reset:
                wait_time = max(1, e.rate_limit_reset - int(time.time()))
                print(f"Rate limit exceeded, retrying in {wait_time} seconds...")
                await asyncio.sleep(wait_time)
            else:
                print("Max retries reached. Exiting.")
                break
        except Exception as e:
            print(f"Error during tweet retrieval: {e}")
            break

    for tweet in all_tweets:
        print(tweet.id)  # Asumiendo que los objetos tweet tienen un atributo id
async def main():
    await client.login(
        auth_info_1=USERNAME,
        auth_info_2=EMAIL,
        password=PASSWORD
    )
    await getTweet()
    """
    poner un tweet
    
    media_ids = [
        await client.upload_media('images.jpeg'),
        await client.upload_media('php.jpg'),

    ]

    await client.create_tweet(
        'este es un tweet de prueba, sin fotos ni videos',
        media_ids=media_ids
    )
    """

asyncio.run(main())



