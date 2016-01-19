"""Celebrities table douban_id column add unique

Revision ID: 5d376584095d
Revises: e7b3dd483603
Create Date: 2016-01-19 18:52:27.455964

"""

# revision identifiers, used by Alembic.
revision = '5d376584095d'
down_revision = 'e7b3dd483603'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('celebrities', schema=None) as batch_op:
        batch_op.create_unique_constraint('celebrities_douban_id_key', ['douban_id'])

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('celebrities', schema=None) as batch_op:
        batch_op.drop_constraint('celebrities_douban_id_key', type_='unique')

    ### end Alembic commands ###
