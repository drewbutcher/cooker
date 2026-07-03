from app import db
from datetime import datetime, timezone

class Ingredient(db.Model):
    __tablename__ = 'ingredients'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id"), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           index=True,
                           default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime(timezone=True),
                           default=lambda: datetime.now(timezone.utc),
                           onupdate=lambda: datetime.now(timezone.utc))
    # Relationships
    recipe = db.relationship("Recipe", back_populates="ingredients")

    # Methods
    def store_in_database(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_database(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        """Model representation for Code Debugging"""
        return f'<Ingredient id:{self.id}>'
