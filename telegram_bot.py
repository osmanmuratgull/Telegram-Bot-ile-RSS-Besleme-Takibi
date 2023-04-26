import feedparser
import telegram
import asyncio

# RSS beslemesi URL'sini belirlemek için kullanılan kod satırı
rss_url = 'https://www.example.com/feed/'

# Telegram botunu bağlamak için ayrılan kod satırı
bot_token = 'Telegram_Token_Giriniz'
chat_id = '@kanal_adınızı_giriniz'
bot = telegram.Bot(token=bot_token)

# Daha önceden görülmüş gönderileri kontrol eden kod satırı
seen_posts = set()

async def send_new_posts():
    while True:
        try:
            # RSS beslemesini analiz edin ve yeni gönderileri alan kod satırı
            feed = feedparser.parse(rss_url)
            new_posts = [post for post in feed.entries if post.id not in seen_posts]

            # Yeni gönderileri Telegram kanalınıza gönderen kod satırı
            for post in new_posts:
                post_title = post.title
                post_url = post.link
                message = f"{post_title}\n{post_url}"
                await bot.send_message(chat_id=chat_id, text=message)
                # Yeni gönderiyi daha önce eklenmiş mi kontrol eden kod satırı
                seen_posts.add(post.id)

            # 1 dakika bekleyin ve yeniden başlatan kod satırı
            await asyncio.sleep(60)

        except Exception as e:
            print(e)
            # Bir hata oluşursa 5 dakika bekleyin ve yeniden başlatan kod satırı
            await asyncio.sleep(300)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(send_new_posts())
    loop.run_forever()
