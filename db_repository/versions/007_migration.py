from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
track = Table('track', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('type', Enum('subtitle', 'caption', 'description', 'chapters', 'metadata')),
    Column('src_lang', String(length=16)),
    Column('parent_video', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['track'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['track'].drop()
