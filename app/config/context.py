from contextvars import ContextVar
from typing import Optional, List

# Middleware
integration_batch_id: ContextVar[Optional[str]] = ContextVar('integration_batch_id', default=None)
document_correlation_id: ContextVar[Optional[str]] = ContextVar('document_correlation_id', default=None)
origin: ContextVar[Optional[str]] = ContextVar('origin', default=None)
document_type: ContextVar[Optional[str]] = ContextVar('document_type', default=None)
documents_error: ContextVar[Optional[List[any]]] = ContextVar('documents_error', default=[])
branch_code: ContextVar[Optional[str]] = ContextVar('branch_code', default=None)


