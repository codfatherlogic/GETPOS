__version__ = '0.0.1'

try:
    from frappe.core.doctype.user.user import User
except ImportError:
    # Frappe not available during installation
    User = None
