"""skillpower table

Revision ID: 5dd5e64fe4a6
Revises: f1a0b7de3ad9
Create Date: 2020-08-11 22:47:54.230252

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5dd5e64fe4a6'
down_revision = 'f1a0b7de3ad9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('skill_power',
    sa.Column('name', sa.String(length=8), nullable=False),
    sa.Column('min_power', sa.Integer(), nullable=True),
    sa.Column('max_power', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('skill_power')
    # ### end Alembic commands ###
