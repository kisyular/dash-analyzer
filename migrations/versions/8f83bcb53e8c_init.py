"""init

Revision ID: 8f83bcb53e8c
Revises: 44066ae74426
Create Date: 2020-01-28 19:41:32.811160

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f83bcb53e8c'
down_revision = '44066ae74426'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('postURL',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=5000), nullable=True),
    sa.Column('website_name', sa.String(length=5000), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_postURL_timestamp'), 'postURL', ['timestamp'], unique=False)
    op.create_table('scrapped_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('browser', sa.String(length=5000), nullable=True),
    sa.Column('time', sa.String(length=5000), nullable=True),
    sa.Column('unique_time', sa.String(length=5000), nullable=True),
    sa.Column('ip_request', sa.String(length=5000), nullable=True),
    sa.Column('country', sa.String(length=5000), nullable=True),
    sa.Column('region', sa.String(length=5000), nullable=True),
    sa.Column('zipcode', sa.String(length=5000), nullable=True),
    sa.Column('city', sa.String(length=5000), nullable=True),
    sa.Column('latitude', sa.String(length=5000), nullable=True),
    sa.Column('longitude', sa.String(length=5000), nullable=True),
    sa.Column('website_name', sa.String(length=5000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('selected_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=5000), nullable=True),
    sa.Column('website_name', sa.String(length=5000), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_selected_data_timestamp'), 'selected_data', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_selected_data_timestamp'), table_name='selected_data')
    op.drop_table('selected_data')
    op.drop_table('scrapped_data')
    op.drop_index(op.f('ix_postURL_timestamp'), table_name='postURL')
    op.drop_table('postURL')
    # ### end Alembic commands ###