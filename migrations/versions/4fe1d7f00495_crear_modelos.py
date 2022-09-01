"""Crear modelos

Revision ID: 4fe1d7f00495
Revises: b371502c5d49
Create Date: 2022-09-01 15:20:26.895304

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fe1d7f00495'
down_revision = 'b371502c5d49'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('nombre', sa.String(), nullable=True),
    sa.Column('apellido', sa.String(), nullable=True),
    sa.Column('direccion', sa.String(), nullable=True),
    sa.Column('telefono', sa.String(), nullable=True),
    sa.Column('correo', sa.String(), nullable=True),
    sa.Column('creacion', sa.DateTime(), nullable=True),
    sa.Column('estado', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('correo'),
    sa.UniqueConstraint('username')
    )
    op.create_table('venta',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.Column('venta', sa.Integer(), nullable=True),
    sa.Column('ventas_productos', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('venta')
    op.drop_table('usuario')
    # ### end Alembic commands ###
