"""empty message

Revision ID: 2b4fb540a535
Revises: 1f3b51ba7d4b
Create Date: 2021-03-20 18:30:20.642103

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b4fb540a535'
down_revision = '1f3b51ba7d4b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("post") as batch_op1: #, op.batch_alter_table("subscribed_user") as batch_op2: 
        batch_op1.drop_column('draft')
        # batch_op2.drop_column('name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subscribed_user', sa.Column('name', sa.VARCHAR(length=20), nullable=True))
    op.add_column('post', sa.Column('draft', sa.INTEGER(), nullable=True))
    # ### end Alembic commands ###
