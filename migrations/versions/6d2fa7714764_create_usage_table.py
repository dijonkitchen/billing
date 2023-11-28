"""create usage table

Revision ID: 6d2fa7714764
Revises: 60da7e737dea
Create Date: 2023-07-03 11:35:25.258527

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "6d2fa7714764"
down_revision = "60da7e737dea"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "usage",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("customer_id", sa.String(length=36)),
        sa.ForeignKeyConstraint(["customer_id"], ["customer.id"]),
        sa.Column("service", sa.String(length=255)),
        sa.Column("units_consumed", sa.Integer()),
        sa.Column("price_per_unit", sa.Numeric(10, 2)),
        sa.Column(
            "created_at",
            sa.DateTime,
            nullable=False,
            server_default=sa.text("CURRENT_TIMESTAMP"),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime,
            nullable=False,
            server_default=sa.text("CURRENT_TIMESTAMP"),
        ),
    )


def downgrade() -> None:
    op.drop_table("usage")
