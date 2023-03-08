import random
from flask import render_template, url_for, flash, redirect, abort
from flask_appbuilder.exceptions import FABException
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, expose, has_access, IndexView

from . import appbuilder, db
from .models import Word
from .widgets import RandomWidget


class WordModelView(ModelView):
    datamodel = SQLAInterface(Word)
    label_columns = {
        'title': 'Word',
        'creation_date': 'Creation date',
        'phonetic': "Phonetic",
        'translation_es': "Spanish",
        'translation_en': "English"
    }
    list_columns = ['title', 'phonetic']
    add_fieldsets = [
        (
            'Word',
            {'fields': ['title', 'phonetic']}
        ),
        (
            'Translations',
            {'fields': ['translation_en', 'translation_es']}
        ),
    ]
    random_columns = ['title']

    def _random(self):
        """
        show function logic, override to implement different logic
        returns show and related list widget
        """

        item_amount, items = self.datamodel.query()
        item = random.choice(items)

        if not item:
            abort(404)
        widget = RandomWidget(
            pk=item.id,
            label_columns=self.label_columns,
            include_columns=self.random_columns,
            value_columns=self.datamodel.get_values_item(item, self.random_columns),
            formatters_columns=self.formatters_columns,
            modelview_name=self.__class__.__name__,
        )
        self.update_redirect()
        return self._get_related_views_widgets(
            item,  widgets={"random": widget}
        )

    @expose("/random")
    @has_access
    def random(self):
        self.update_redirect()
        try:
            widgets = self._random()
        except FABException as exc:
            flash(f"An error occurred: {exc}", "warning")
            return redirect(self.get_redirect())
        return self.render_template(
            template="appbuilder/general/model/random_word.html",
            title="Random word",
            widgets=widgets
        )


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    """Application wide 404 error handler"""
    return (
        render_template(
            "404.html",
            base_template=appbuilder.base_template,
            appbuilder=appbuilder,
        ),
        404,
    )


db.create_all()
db.event.listen(Word.title, 'set', Word.slugify, retval=False)

# Activate views

appbuilder.add_view(
    WordModelView,
    "Words list",
    icon="fa-list",
    category="Words",
    category_icon="fa-w"
)
appbuilder.add_link(
    "Random words",
    href="/wordmodelview/random",
    icon="fa-shuffle",
    category="Words"
)
