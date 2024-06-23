import finnhub

def scrape_news():
    finnhub_client = finnhub.Client(api_key="cponss1r01qiv403hs00cponss1r01qiv403hs0g")

    news = finnhub_client.general_news('general', min_id=0)

    return news
