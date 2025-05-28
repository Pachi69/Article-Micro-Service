from typing import List
from app.models import Brand
from app.repositories import BrandRepository
from app import cache


class BrandService():

    @staticmethod
    def save(brand:Brand) -> 'Brand':
        BrandRepository.save(brand)
        cache.set(f'brand_{brand.id}', brand, timeout=15)
        return brand
    
    @staticmethod
    def delete(brand:Brand) -> None:
        BrandRepository.delete(brand)
        cache.delete(f'brand_{brand.id}')

    @staticmethod
    def find(id: int) -> 'Brand':
        result = cache.get(f'brand_{id}')
        if result is None:
            result = BrandRepository.find(id)
            cache.set(f'brand_{id}', result, timeout=15)
        return BrandRepository.find(id)

    @staticmethod
    def find_all() -> List['Brand']:
        result = cache.get('articles')
        if result is None:
            result = BrandRepository.find_all()
            cache.set('articles', result, timeout=15)
        return BrandRepository.find_all()
    
    @staticmethod
    def find_by(**kwargs) -> List['Brand']:
        return BrandRepository.find_by(**kwargs)
    
    @staticmethod
    def update(brand: 'Brand') -> 'Brand':
        BrandRepository.update(brand)
        cache.set(f'brand_{brand.id}', brand, timeout=15)
        return brand