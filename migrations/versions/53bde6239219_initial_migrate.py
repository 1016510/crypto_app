"""initial migrate

Revision ID: 53bde6239219
Revises: 
Create Date: 2021-07-15 11:18:33.376830

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53bde6239219'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cryptozaken',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('zaaknaam', sa.String(length=64), nullable=True),
    sa.Column('verdachte', sa.String(length=64), nullable=True),
    sa.Column('currency', sa.String(length=64), nullable=True),
    sa.Column('aantal', sa.Float(), nullable=True),
    sa.Column('totale_waarde', sa.Float(), nullable=True),
    sa.Column('datum_tijd', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cryptozaken')
    # ### end Alembic commands ###