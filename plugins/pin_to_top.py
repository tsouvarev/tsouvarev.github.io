"""
Pin to top plugin for Pelican
================================

Adds .pin variable to article's context and pins the article to the top
 even if it is older than the other articles
"""

from itertools import count
from pelican import signals


def update_pinned_articles(generator):
    new_order = []
    pin_count = count()

    for article in generator.articles:
        if hasattr(article, "pin"):
            new_order.insert(next(pin_count), article)
        else:
            new_order.append(article)

    generator.articles = new_order
    generator.context["articles"] = generator.articles


def register():
    signals.article_generator_finalized.connect(update_pinned_articles)
