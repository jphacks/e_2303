"""[fix] report table structure

Revision ID: c6098d662989
Revises: 2d4537ebb49f
Create Date: 2023-10-28 05:28:59.988939

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'c6098d662989'
down_revision: Union[str, None] = '2d4537ebb49f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('report', sa.Column('no', sa.Integer(), nullable=False))
    op.add_column('report', sa.Column('emotion_score', sa.Float(), nullable=True))
    op.add_column('report', sa.Column('emotion_magnitude', sa.Float(), nullable=True))
    op.add_column('report', sa.Column('target', sa.String(), nullable=False))
    op.add_column('report', sa.Column('scheduled_hearing_date', sa.DateTime(), nullable=False))
    op.add_column('report', sa.Column('hearing_date', sa.DateTime(), nullable=True))
    op.drop_column('report', 'emotion')
    op.drop_column('report', 'next_date')
    op.drop_column('report', 'next_target')
    op.drop_column('report', 'is_initial')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('report', sa.Column('is_initial', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('report', sa.Column('next_target', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('report', sa.Column('next_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.add_column('report', sa.Column('emotion', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.drop_column('report', 'hearing_date')
    op.drop_column('report', 'scheduled_hearing_date')
    op.drop_column('report', 'target')
    op.drop_column('report', 'emotion_magnitude')
    op.drop_column('report', 'emotion_score')
    op.drop_column('report', 'no')
    # ### end Alembic commands ###
