from app import db
from datetime import datetime, timezone

class Tip(db.Model):
    __tablename__ = 'tips'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    cook_step_id = db.Column(db.Integer, db.ForeignKey("cook_steps.id"), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           index=True,
                           default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime(timezone=True),
                           default=lambda: datetime.now(timezone.utc),
                           onupdate=lambda: datetime.now(timezone.utc))
    # Relationships
    cook_step = db.relationship("CookStep", back_populates="tips")

    # Methods
    def store_in_database(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_database(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        """Model representation for Code Debugging"""
        return f'<Tip id:{self.id}>'
