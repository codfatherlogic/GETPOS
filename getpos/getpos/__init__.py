# Instead of importing at module level
# from frappe.core.doctype.user.user import User

# Move it inside functions where it's needed
def some_function():
    from frappe.core.doctype.user.user import User
    # ... rest of your code
