from datetime import date
from flask_appbuilder import Model
from slugify import slugify as string_slugify
from sqlalchemy import Column, Integer, String, Date, Identity


class Word(Model):
    id = Column(Integer, Identity(start=1), primary_key=True)
    slug = Column(String(150), unique=True, nullable=False)
    title = Column(String(150), nullable=False)
    creation_date = Column(Date, default=date.today())
    phonetic = Column(String(150))
    translation_en = Column(String(150))
    translation_es = Column(String(150))

    def __repr__(self):
        return f"<Word {self.title}>"

    @staticmethod
    def slugify(target, value, oldvalue, initiator):
        if value and (not target.slug or value != oldvalue):
            target.slug = string_slugify(value)
