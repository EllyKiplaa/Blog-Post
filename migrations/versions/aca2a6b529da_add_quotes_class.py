"""Add quotes class

Revision ID: aca2a6b529da
Revises: 981a9bd29d0c
Create Date: 2020-07-23 02:28:24.790649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aca2a6b529da'
down_revision = '981a9bd29d0c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subscribers')
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('email', sa.String(), nullable=False))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    op.alter_column('users', 'password_hash',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.create_unique_constraint(None, 'users', ['email'])
    op.create_unique_constraint(None, 'users', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'users', type_='unique')
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('users', 'password_hash',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'email')
    op.drop_column('users', 'bio')
    op.create_table('subscribers',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('subscriber_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('subscriber_email', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='subscribers_pkey'),
    sa.UniqueConstraint('subscriber_email', name='subscribers_subscriber_email_key')
    )
    # ### end Alembic commands ###
