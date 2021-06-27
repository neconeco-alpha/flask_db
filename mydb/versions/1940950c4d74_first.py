"""first

Revision ID: 1940950c4d74
Revises:
Create Date: 2021-06-25 20:27:45.067133

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1940950c4d74'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )



def downgrade():
    op.drop_table('account')
