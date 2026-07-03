from app import db
from datetime import datetime, timezone

class Image(db.Model):
    __tablename__ = 'images'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    comment_id = db.Column(db.Integer, db.ForeignKey("comments.id"), nullable=False)
    alt_text = db.Column(db.String(512), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           index=True,
                           default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime(timezone=True),
                           default=lambda: datetime.now(timezone.utc),
                           onupdate=lambda: datetime.now(timezone.utc))

    # Relationships
    comment = db.relationship("Comment", back_populates="images")

    # Methods
    def store_in_database(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_database(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        """Model representation for Code Debugging"""
        return f'<Image id:{self.id}>'
