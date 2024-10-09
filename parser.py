import feedparser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import NewsArticle  # Assume models.py defines the SQLAlchemy model for the articles

# Database setup
DATABASE_URL = "postgresql://username:password@localhost:5432/news_db"  # Update with your DB credentials
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# List of RSS feeds
rss_feeds = [
    "http://rss.cnn.com/rss/cnn_topstories.rss",
    "http://qz.com/feed",
    "http://feeds.foxnews.com/foxnews/politics",
    "http://feeds.reuters.com/reuters/businessNews",
    "http://feeds.feedburner.com/NewshourWorld",
    "https://feeds.bbci.co.uk/news/world/asia/india/rss.xml",
]

def parse_feeds():
    for feed in rss_feeds:
        print(f"Parsing {feed}")
        articles = feedparser.parse(feed).entries
        for article in articles:
            title = article.title
            content = article.summary
            pub_date = article.published
            source_url = article.link
            
            # Check for duplicates
            if not session.query(NewsArticle).filter_by(title=title, source_url=source_url).first():
                new_article = NewsArticle(title=title, content=content, publication_date=pub_date, source_url=source_url)
                session.add(new_article)
                session.commit()
                print(f"Added article: {title}")

if __name__ == "__main__":
    parse_feeds()
