"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref
import enum

class Event_type(enum.Enum):
    PARTY = 1
    STUDY = 2
    NETWORKING = 3
    CONFERENCE = 4

class Guest(db.Model):
    '''Guest model'''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(15), nullable=False)

    events_attending = db.relationship('Event', secondary='guest_event', back_populates='guests')

    def __repr__(self):
        return f'{self.name}'

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    date_and_time = db.Column(db.DateTime, nullable=False)

    event_type = db.Column(db.Enum(Event_type), default=Event_type.CONFERENCE)

    guests = db.relationship('Guest', secondary='guest_event', back_populates='events_attending')

    def __repr__(self):
        return f'{self.title}'


guest_event = db.Table('guest_event',
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
    )