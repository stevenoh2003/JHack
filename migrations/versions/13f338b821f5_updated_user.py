"""Updated User

Revision ID: 13f338b821f5
Revises: d0903640b103
Create Date: 2021-04-14 18:44:37.231304

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13f338b821f5'
down_revision = 'd0903640b103'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_table('_alembic_tmp_user')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('age', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('date_joined', sa.DateTime(), nullable=True))
        batch_op.drop_column('grade')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('grade', sa.INTEGER(), nullable=True))
        batch_op.drop_column('date_joined')
        batch_op.drop_column('age')

    op.create_table('_alembic_tmp_user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=20), nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), nullable=False),
    sa.Column('password', sa.VARCHAR(length=60), nullable=False),
    sa.Column('role', sa.VARCHAR(length=10), nullable=True),
    sa.Column('first_name', sa.VARCHAR(length=20), nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=20), nullable=True),
    sa.Column('responsibility', sa.TEXT(), nullable=True),
    sa.Column('age', sa.INTEGER(), nullable=True),
    sa.Column('date_joined', sa.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('id', name='pk_user'),
    sa.UniqueConstraint('email', name='uq_user_email'),
    sa.UniqueConstraint('username', name='uq_user_username')
    )
    # ### end Alembic commands ###
