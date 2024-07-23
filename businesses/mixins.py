from django.contrib.auth.mixins import UserPassesTestMixin

class PowerUserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.has_perm('businesses.add_business')
