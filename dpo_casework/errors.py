"""Package-specific exceptions for casework operations."""

from __future__ import annotations


class CaseworkError(Exception):
    """Base class for casework errors."""


class CaseworkPayloadError(CaseworkError, ValueError):
    """Raised when a casework payload is incomplete or invalid."""
