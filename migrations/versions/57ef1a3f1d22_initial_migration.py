"""Initial migration.

Revision ID: 57ef1a3f1d22
Revises: 
Create Date: 2021-01-21 17:15:13.816196

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '57ef1a3f1d22'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recipient_alias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('alias', sqlalchemy_utils.types.email.EmailType(length=255), nullable=True, comment='The "To" address that should be redirected'),
    sa.Column('recipient', sqlalchemy_utils.types.email.EmailType(length=255), nullable=True, comment='The "To" address to redirect to'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_recipient_alias'))
    )
    op.create_table('sender_alias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sender', sa.String(length=120), nullable=True, comment='The username of the sender who has this alias'),
    sa.Column('alias', sqlalchemy_utils.types.email.EmailType(length=255), nullable=True, comment='The email address for which the sender is allowed to send as'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_sender_alias'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sender_alias')
    op.drop_table('recipient_alias')
    # ### end Alembic commands ###
