from django.views.generic import CreateView


class LandingPageView(CreateView):

    template_name = 'site/landing.html'

    def get_success_url(self):
        return '{}?signup_success=1'.format(self.request.path)
