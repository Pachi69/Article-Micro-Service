from app.models import Article
from app.repositories import ArticleRepository
from typing import List
from app import cache


class ArticleService():
    
    @staticmethod
    def save(article: Article) -> 'Article':
        ArticleRepository.save(article)
        cache.set(f'article_{article.id}', article, timeout=15)
        return article
    
    @staticmethod
    def delete(article: 'Article') -> None:
        ArticleRepository.delete(article)
        cache.delete(f'article_{article.id}')
    
    @staticmethod
    def find(id: int) -> 'Article':
        article_service = ArticleRepository.find(id)
        result = cache.get(f'articles_{id}')
        if result is None:
             result = ArticleRepository.find(id)
             cache.set(f'articles_{id}', result, timeout=15)
        if not article_service:
                    raise ValueError(f"Article with ID {id} not found.")
        return article_service
    
    @staticmethod
    def find_all() -> List['Article']:
        result = cache.get('articles')
        if result is None:
             result = ArticleRepository.find_all()
             cache.set('articles', result, timeout=15)
        return ArticleRepository.find_all()
    
    @staticmethod
    def find_by(**kwargs) -> List['Article']:
        return ArticleRepository.find_by(**kwargs)
    
    @staticmethod
    def update(article: 'Article') -> 'Article':
        ArticleRepository.update(article)
        cache.set(f'article_{article.id}', article, timeout=15)
        return article