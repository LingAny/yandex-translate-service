from translator_api.lib.async_data_context.errors.sql_error import SqlError


class ForeignKeyViolationError(SqlError):
    pass
