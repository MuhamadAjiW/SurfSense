"""Add LINKUP_API to SearchSourceConnectorType enum

Revision ID: 4
Revises: 3

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4'
down_revision: Union[str, None] = '3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    
    # Manually add the command to add the enum value
    op.execute("ALTER TYPE searchsourceconnectortype ADD VALUE 'LINKUP_API'")
    
    # Pass for the rest, as autogenerate didn't run to add other schema details
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    
    # Downgrading removal of an enum value requires recreating the type
    op.execute("ALTER TYPE searchsourceconnectortype RENAME TO searchsourceconnectortype_old")
    op.execute("CREATE TYPE searchsourceconnectortype AS ENUM('SERPER_API', 'TAVILY_API', 'SLACK_CONNECTOR', 'NOTION_CONNECTOR', 'GITHUB_CONNECTOR', 'LINEAR_CONNECTOR')")
    op.execute((
        "ALTER TABLE search_source_connectors ALTER COLUMN connector_type TYPE searchsourceconnectortype USING "
        "connector_type::text::searchsourceconnectortype"
    ))
    op.execute("DROP TYPE searchsourceconnectortype_old")

    pass
    # ### end Alembic commands ### 