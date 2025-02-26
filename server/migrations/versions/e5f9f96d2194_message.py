"""message

Revision ID: e5f9f96d2194
Revises: d4d8da40c2f3
Create Date: 2025-01-27 13:36:38.786274

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5f9f96d2194'
down_revision = 'd4d8da40c2f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pizza_id', sa.Integer(), nullable=True))
        batch_op.alter_column('restaurant_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.create_foreign_key(batch_op.f('fk_restaurant_pizzas_pizza_id_pizzas'), 'pizzas', ['pizza_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_restaurant_pizzas_pizza_id_pizzas'), type_='foreignkey')
        batch_op.alter_column('restaurant_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.drop_column('pizza_id')

    # ### end Alembic commands ###
