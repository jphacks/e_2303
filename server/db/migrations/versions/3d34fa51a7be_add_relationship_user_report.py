"""add relationship user-report

Revision ID: 3d34fa51a7be
Revises: 4b7ba426d4f7
Create Date: 2023-10-28 21:40:14.360797

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3d34fa51a7be'
down_revision: Union[str, None] = '4b7ba426d4f7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
