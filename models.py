from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class NewsArticle(Base):
    __tablename__ = 'news_articles'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)  # Ensuring no duplicates by title
    content = Column(String)
    publication_date = Column(DateTime)
    source_url = Column(String)

# Create the database tables
if __name__ == "__main__":
    from sqlalchemy import create_engine
    engine = create_engine("postgresql://username:password@localhost:5432/news_db")  # Update with your DB credentials
    Base.metadata.create_all(engine)
