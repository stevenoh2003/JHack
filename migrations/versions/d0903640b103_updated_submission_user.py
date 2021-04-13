"""Updated Submission, User

Revision ID: d0903640b103
Revises: 2b4fb540a535
Create Date: 2021-04-13 19:38:15.586556

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0903640b103'
down_revision = '2b4fb540a535'
branch_labels = None
depends_on = None

convention = {
    'pk': 'pk_%(table_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'ix': 'ix_%(table_name)s_%(column_0_name)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(column_0_name)s',
}

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_submission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('submission_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['submission_id'], ['submission.id'], name=op.f('fk_user_submission_submission_id_submission')),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_user_submission_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user_submission'))
    )
    with op.batch_alter_table('submission', schema=None, naming_convention=convention) as batch_op:
        batch_op.add_column(sa.Column('code', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('draft', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('editable', sa.Boolean(), nullable=True))
        batch_op.alter_column('school_name',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
        batch_op.alter_column('team_name',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
        batch_op.drop_constraint('fk_submission_user_id_user', type_='foreignkey')
        batch_op.drop_column('user_id')

    with op.batch_alter_table('user', schema=None, naming_convention=convention) as batch_op:
        batch_op.add_column(sa.Column('first_name', sa.String(length=20), nullable=True))
        batch_op.add_column(sa.Column('grade', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('last_name', sa.String(length=20), nullable=True))
        batch_op.add_column(sa.Column('responsibility', sa.Text(), nullable=True))
        batch_op.drop_column('bio')
        batch_op.drop_column('image_file')
        batch_op.drop_column('gender')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None, naming_convention=convention) as batch_op:
        batch_op.add_column(sa.Column('gender', sa.VARCHAR(length=20), nullable=True))
        batch_op.add_column(sa.Column('image_file', sa.VARCHAR(length=20), nullable=False))
        batch_op.add_column(sa.Column('bio', sa.VARCHAR(length=400), nullable=True))
        batch_op.drop_column('responsibility')
        batch_op.drop_column('last_name')
        batch_op.drop_column('grade')
        batch_op.drop_column('first_name')

    with op.batch_alter_table('submission', schema=None, naming_convention=convention) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), nullable=False))
        batch_op.create_foreign_key('fk_submission_user_id_user', 'user', ['user_id'], ['id'])
        batch_op.alter_column('team_name',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
        batch_op.alter_column('school_name',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
        batch_op.drop_column('editable')
        batch_op.drop_column('draft')
        batch_op.drop_column('code')

    op.drop_table('user_submission')
    # ### end Alembic commands ###