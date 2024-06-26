"""rename department

Revision ID: 18b26a56563f
Revises: 9427ec8d4d9b
Create Date: 2024-04-01 20:43:39.059550

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18b26a56563f'
down_revision = '9427ec8d4d9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
