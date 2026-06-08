# Make sure all models are imported here for Alembic
from app.db.base import Base
from app.models.user import User, SocialIdentity
from app.models.profile import Profile
from app.models.work import Work, WorkCredit
from app.models.project import Project, Character
from app.models.offer import Offer
