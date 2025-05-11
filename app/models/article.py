from dataclasses import dataclass
from app import db


@dataclass(init=True, eq=False)
class Article(db.Model):
    """
    Article con sus atributos
    """
    __tablename__ = 'articles'
    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column('name', db.String[100], nullable=False)
    description: str = db.Column('description', db.String[150], nullable=False)
    id_category: int = db.Column('id_category', db.Integer, db.ForeignKey('categories.id'))
    id_brand: int = db.Column('id_brand', db.Integer, db.ForeignKey('brands.id'))
    minimun_stock: int = db.Column('minimun_stock', db.Float, nullable=False)
    code_ean13: str = db.Column('code_ean13', db.String[150], nullable=False)
    brand = db.relationship('Brand')
    category = db.relationship('Category')
    
    def __eq__(self, article:object) -> bool:
        return self.name == article.name and self.code_ean13 == article.code_ean13