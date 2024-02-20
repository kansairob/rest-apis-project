"""empty message

Revision ID: c3ec716ee7a9
Revises: b9863a99cb84
Create Date: 2024-02-15 21:51:18.167860

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3ec716ee7a9'
down_revision = 'b9863a99cb84'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(), nullable=False))
        batch_op.create_unique_constraint("email", ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint("email", type_='unique')
        batch_op.drop_column('email')

    # ### end Alembic commands ###