from app.models import Category
from app.repositories import CategoryRepository
from typing import List
from app import cache


class CategoryService():
    
    @staticmethod
    def save(category: Category) -> 'Category':
        cache.set(f'category_{category.id}', category, timeout=15)
        CategoryRepository.save(category)
        return category
    
    @staticmethod
    def delete(category: 'Category') -> None:
        CategoryRepository.delete(category)
        cache.delete(f'category_{category.id}')

    @staticmethod
    def find(id: int) -> 'Category':
        result = cache.get(f'category_{id}')
        if result is None:
            result = CategoryRepository.find(id)
            cache.set(f'category_{id}', result, timeout=15)
        return CategoryRepository.find(id)
    
    @staticmethod
    def find_all() -> List['Category']:
        result = cache.get('categories')
        if result is None:
            result = CategoryRepository.find_all()
            cache.set('articles', result, timeout=15)
        return CategoryRepository.find_all()
    
    @staticmethod
    def find_by(**kwargs) -> List['Category']:
        return CategoryRepository.find_by(**kwargs)
    
    @staticmethod
    def update(category: 'Category') -> 'Category':
        CategoryRepository.update(category)
        cache.set(f'category_{category.id}', category, timeout=15)
        return category