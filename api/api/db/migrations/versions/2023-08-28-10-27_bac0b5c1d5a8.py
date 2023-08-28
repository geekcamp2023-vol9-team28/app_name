"""Add users table

Revision ID: bac0b5c1d5a8
Revises: 2b7380507a71
Create Date: 2023-08-28 10:27:58.125806

"""
import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op

# revision identifiers, used by Alembic.
revision = "bac0b5c1d5a8"
down_revision = "2b7380507a71"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column(
            "email", sqlalchemy_utils.types.email.EmailType(length=255), nullable=False
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.alter_column(
        "dummy_model", "name", existing_type=sa.VARCHAR(length=200), nullable=False
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "dummy_model", "name", existing_type=sa.VARCHAR(length=200), nullable=True
    )
    op.drop_table("users")
    # ### end Alembic commands ###