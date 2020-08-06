"""quest and item tables

Revision ID: 0c9defccff22
Revises: 5f699fb118d9
Create Date: 2020-08-06 23:24:12.565455

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c9defccff22'
down_revision = '5f699fb118d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quest',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('item_drop',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_name', sa.String(length=64), nullable=True),
    sa.Column('item_count', sa.Integer(), nullable=True),
    sa.Column('quest_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['quest_id'], ['quest.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('item_drop')
    op.drop_table('quest')
    # ### end Alembic commands ###