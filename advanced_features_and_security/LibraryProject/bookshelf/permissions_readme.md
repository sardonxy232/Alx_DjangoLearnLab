## Permissions and Groups Setup

We use Django's built-in permission system to secure views based on user roles.

### Custom Permissions Added (in Book model):
- can_view: Allows reading/viewing book list
- can_create: Allows adding new books
- can_edit: Allows editing existing books
- can_delete: Allows deleting books

### Groups:
- Viewers: `can_view`
- Editors: `can_view`, `can_create`, `can_edit`
- Admins: All permissions

### Enforced in Views:
Permissions are enforced using `@permission_required` decorators.
