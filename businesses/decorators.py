from django.contrib.auth.decorators import user_passes_test

def admin_required(view_func):
    """
    Decorator to ensure that only superusers (admins) can access the view.
    """
    decorated_view_func = user_passes_test(lambda u: u.is_superuser)(view_func)
    return decorated_view_func
