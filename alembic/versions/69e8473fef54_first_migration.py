"""First migration

Revision ID: 69e8473fef54
Revises: 
Create Date: 2022-12-29 03:56:59.201610

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '69e8473fef54'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meetingroom',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('meetingroom')
    # ### end Alembic commands ###
