from app import db
from datetime import datetime, timezone

class Comment(db.Model):
    __tablename__ = 'comments'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id"), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           index=True,
                           default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime(timezone=True),
                           default=lambda: datetime.now(timezone.utc),
                           onupdate=lambda: datetime.now(timezone.utc))

    # Relationships
    author = db.relationship("User", back_populates="comments")
    recipe = db.relationship("Recipe", back_populates="comments")
    images = db.relationship("Image", back_populates="comment", cascade="all, delete-orphan")


    # Methods
    def store_in_database(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_database(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        """Model representation for Code Debugging"""
        return f'<Comment id:{self.id}>'
