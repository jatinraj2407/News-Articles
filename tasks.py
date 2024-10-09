from celery import Celery
from nlp import classify_article  # Assume classify_article uses NLTK or spaCy

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def process_article(article_id):
    session = Session()
    article = session.query(NewsArticle).get(article_id)
    if article:
        category = classify_article(article.content)
        article.category = category
        session.commit()
        print(f"Article {article.title} classified as {category}")
