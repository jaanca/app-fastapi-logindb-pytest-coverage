"""Quitar columna user.estado2

Revision ID: 8f3b0c1bb07a
Revises: 83094284c964
Create Date: 2022-08-25 20:38:48.196198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f3b0c1bb07a'
down_revision = '83094284c964'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuario', 'estado2')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuario', sa.Column('estado2', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
