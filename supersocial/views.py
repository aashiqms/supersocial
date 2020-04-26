from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'index.html'


class TestPage(TemplateView):
    template_name = 'index.html'


class ThanksPage(TemplateView):
    template_name = 'index.html'


home_page_view = HomePage.as_view()
test_page_view = TestPage.as_view()
thanks_page_view = ThanksPage.as_view()
