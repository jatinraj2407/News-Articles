# News Article Aggregator

This project is designed to collect news articles from various RSS feeds, store them in a database, and categorize them into predefined categories.

## Getting Started

### Prerequisites

- Python 3.x
- PostgreSQL
- Redis (for Celery)
- Required Python libraries (see requirements.txt)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/NewsArticleAggregator.git
   cd NewsArticleAggregator
   ```
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your PostgreSQL database and update the DATABASE_URL in `models.py` and `parser.py`.
4. Start the Redis server for Celery.

### Running the Application

- Run the feed parser:
  ```bash
  python parser.py
  ```
- Start the Celery worker:
  ```bash
  celery -A tasks worker --loglevel=info
  ```
