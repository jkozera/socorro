"""bug 895928 Signature Summary tables

Revision ID: 11cd71153550
Revises: 54e898dc3251
Create Date: 2013-07-23 13:38:20.141205

"""

# revision identifiers, used by Alembic.
revision = '11cd71153550'
down_revision = '54e898dc3251'

import os
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql
from sqlalchemy import types
from sqlalchemy.sql import table, column
try:
    from sqlalchemy.dialects.postgresql import *
    from sqlalchemy.dialects.postgresql.base import ischema_names
except ImportError:
    from sqlalchemy.databases.postgres import *



class CITEXT(types.UserDefinedType):
    name = 'citext'

    def get_col_spec(self):
        return 'CITEXT'

    def bind_processor(self, dialect):
        return lambda value: value

    def result_processor(self, dialect, coltype):
        return lambda value: value

    def __repr__(self):
        return "citext"

class JSON(types.UserDefinedType):
    name = 'json'

    def get_col_spec(self):
        return 'JSON'

    def bind_processor(self, dialect):
        return lambda value: value

    def result_processor(self, dialect, coltype):
        return lambda value: value

    def __repr__(self):
        return "json"

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table(u'signature_summary_installations',
    sa.Column(u'signature_id', sa.INTEGER(), nullable=False),
    sa.Column(u'product_name', sa.TEXT(), nullable=False),
    sa.Column(u'version_string', sa.TEXT(), nullable=False),
    sa.Column(u'report_date', sa.DATE(), nullable=False),
    sa.Column(u'crash_count', sa.INTEGER(), nullable=False),
    sa.Column(u'install_count', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['signature_id'], [u'signatures.signature_id'], ),
    sa.PrimaryKeyConstraint(u'signature_id', u'product_name', u'version_string', u'report_date')
    )
    op.create_table(u'signature_summary_products',
    sa.Column(u'signature_id', sa.INTEGER(), nullable=False),
    sa.Column(u'product_version_id', sa.INTEGER(), nullable=False),
    sa.Column(u'product_name', sa.TEXT(), nullable=False),
    sa.Column(u'version_string', sa.TEXT(), nullable=False),
    sa.Column(u'report_date', sa.DATE(), nullable=False),
    sa.Column(u'report_count', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['product_version_id'], [u'product_versions.product_version_id'], ),
    sa.ForeignKeyConstraint(['signature_id'], [u'signatures.signature_id'], ),
    sa.PrimaryKeyConstraint(u'signature_id', u'product_version_id', u'report_date')
    )
    op.create_table(u'signature_summary_os',
    sa.Column(u'signature_id', sa.INTEGER(), nullable=False),
    sa.Column(u'os_version_string', sa.TEXT(), nullable=False),
    sa.Column(u'product_version_id', sa.INTEGER(), nullable=False),
    sa.Column(u'product_name', sa.TEXT(), nullable=False),
    sa.Column(u'report_date', sa.DATE(), nullable=False),
    sa.Column(u'report_count', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['product_version_id'], [u'product_versions.product_version_id'], ),
    sa.ForeignKeyConstraint(['signature_id'], [u'signatures.signature_id'], ),
    sa.PrimaryKeyConstraint(u'signature_id', u'os_version_string', u'product_version_id', u'report_date')
    )
    op.create_table(u'signature_summary_process_type',
    sa.Column(u'signature_id', sa.INTEGER(), nullable=False),
    sa.Column(u'process_type', sa.TEXT(), nullable=False),
    sa.Column(u'product_version_id', sa.INTEGER(), nullable=False),
    sa.Column(u'product_name', sa.TEXT(), nullable=False),
    sa.Column(u'report_date', sa.DATE(), nullable=False),
    sa.Column(u'report_count', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['product_version_id'], [u'product_versions.product_version_id'], ),
    sa.ForeignKeyConstraint(['signature_id'], [u'signatures.signature_id'], ),
    sa.PrimaryKeyConstraint(u'signature_id', u'process_type', u'product_version_id', u'report_date')
    )
    op.create_table(u'signature_summary_flash_version',
    sa.Column(u'signature_id', sa.INTEGER(), nullable=False),
    sa.Column(u'flash_version', sa.TEXT(), nullable=False),
    sa.Column(u'product_version_id', sa.INTEGER(), nullable=False),
    sa.Column(u'product_name', sa.TEXT(), nullable=False),
    sa.Column(u'report_date', sa.DATE(), nullable=False),
    sa.Column(u'report_count', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['product_version_id'], [u'product_versions.product_version_id'], ),
    sa.ForeignKeyConstraint(['signature_id'], [u'signatures.signature_id'], ),
    sa.PrimaryKeyConstraint(u'signature_id', u'flash_version', u'product_version_id', u'report_date')
    )
    op.create_table(u'signature_summary_uptime',
    sa.Column(u'signature_id', sa.INTEGER(), nullable=False),
    sa.Column(u'uptime_string', sa.TEXT(), nullable=False),
    sa.Column(u'product_version_id', sa.INTEGER(), nullable=False),
    sa.Column(u'product_name', sa.TEXT(), nullable=False),
    sa.Column(u'report_date', sa.DATE(), nullable=False),
    sa.Column(u'report_count', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['product_version_id'], [u'product_versions.product_version_id'], ),
    sa.ForeignKeyConstraint(['signature_id'], [u'signatures.signature_id'], ),
    sa.PrimaryKeyConstraint(u'signature_id', u'uptime_string', u'product_version_id', u'report_date')
    )
    op.create_table(u'signature_summary_architecture',
    sa.Column(u'signature_id', sa.INTEGER(), nullable=False),
    sa.Column(u'architecture', sa.TEXT(), nullable=False),
    sa.Column(u'product_version_id', sa.INTEGER(), nullable=False),
    sa.Column(u'product_name', sa.TEXT(), nullable=False),
    sa.Column(u'report_date', sa.DATE(), nullable=False),
    sa.Column(u'report_count', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['product_version_id'], [u'product_versions.product_version_id'], ),
    sa.ForeignKeyConstraint(['signature_id'], [u'signatures.signature_id'], ),
    sa.PrimaryKeyConstraint(u'signature_id', u'architecture', u'product_version_id', u'report_date')
    )

    app_path=os.getcwd()
    procs = [
              'update_signature_summary.sql'
            , 'backfill_signature_summary.sql'
            , 'backfill_matviews.sql'
            ]
    for myfile in [app_path + '/socorro/external/postgresql/raw_sql/procs/' + line for line in procs]:
        proc = open(myfile, 'r').read()
        op.execute(proc)


    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table(u'signature_summary_architecture')
    op.drop_table(u'signature_summary_uptime')
    op.drop_table(u'signature_summary_flash_version')
    op.drop_table(u'signature_summary_process_type')
    op.drop_table(u'signature_summary_os')
    op.drop_table(u'signature_summary_products')
    op.drop_table(u'signature_summary_installations')
    ### end Alembic commands ###
