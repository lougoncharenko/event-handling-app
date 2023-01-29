"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref

# TODO: Create a model called `Guest` with the following fields:
# - id: primary key
# - name: String column
# - email: String column
# - phone: String column
# - events_attending: relationship to "Event" table with a secondary table
class Event_type (enum.Enum):
    PARTY = 1
    STUDY = 2
    NETWORKING = 3
    CONFERENCE = 4

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    
    # events_attending = db.Column(db.String(80), nullable=False)
    events_attending.id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    events_attending = db.relationship('Event', secondary='guest_event', back_populates='guests')

    def __str__(self):
        return f'<Guest: {self.name}>'

    def __repr__(self):
        return f'<Guest: {self.name} Email: {self.email}>'

# TODO: Create a model called `Event` with the following fields:
# - id: primary key
# - title: String column
# - description: String column
# - date_and_time: DateTime column
# - guests: relationship to "Guest" table with a secondary table

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    date_and_time = db.Column(db.DateTime, nullable=False)

    event_type = db.Column(db.Enum(Event_type), default=Event_type.CONFERENCE)

    guest_id = db.Column(db.Integer, db.ForeignKey('guest.id'), nullable=False)
    guests = db.relationship('Guest', secondary='guest_event', back_populates='events_attending')


# STRETCH CHALLENGE: Add a field `event_type` as an Enum column that denotes the
# type of event (Party, Study, Networking, etc)


# TODO: Create a table `guest_event_table` with the following columns:
# - event_id: Integer column (foreign key)
# - guest_id: Integer column (foreign key)


guest_event_table = db.Table('guest_event',
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
)