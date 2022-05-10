"""Added a Caretaker Model

Revision ID: 7b406d48aa56
Revises: 1c95c64fc74b
Create Date: 2022-05-10 10:00:13.219178

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b406d48aa56'
down_revision = '1c95c64fc74b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('caretaker',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('caretaker')
    # ### end Alembic commands ###
