from app import db
from datetime import datetime, timezone

class CookStep(db.Model):
    __tablename__ = 'cook_steps'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id"), nullable=False)
    sequence = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(256), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           index=True,
                           default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime(timezone=True),
                           default=lambda: datetime.now(timezone.utc),
                           onupdate=lambda: datetime.now(timezone.utc))
    # Relationships
    recipe = db.relationship("Recipe", back_populates="cook_steps")
    tips = db.relationship("Tip", back_populates="cook_step", cascade="all, delete-orphan")

    # Methods
    def store_in_database(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_database(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        """Model representation for Code Debugging"""
        return f'<CookStep id:{self.id}>'
