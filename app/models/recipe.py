from app import db
from datetime import datetime, timezone

class Recipe(db.Model):
    __tablename__ = 'recipes'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False, unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True),
                           index=True,
                           default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime(timezone=True),
                           default=lambda: datetime.now(timezone.utc),
                           onupdate=lambda: datetime.now(timezone.utc))
    # Relationships
    author = db.relationship("User", back_populates="recipes")
    comments = db.relationship(
        "Comment",
        back_populates="recipe",
        foreign_keys="Comment.recipe_id",
        cascade="all, delete-orphan")
    ingredients = db.relationship(
        "Ingredient",
        back_populates="recipe",
        foreign_keys="Ingredient.recipe_id",
        cascade="all, delete-orphan")
    cook_steps = db.relationship(
        "CookStep",
        back_populates="recipe",
        foreign_keys="CookStep.recipe_id",
        cascade="all, delete-orphan")

    # Methods
    def store_in_database(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_database(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        """Model representation for Code Debugging"""
        return f'<Recipe id:{self.id}>'
