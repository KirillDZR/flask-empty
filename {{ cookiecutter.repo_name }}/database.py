# -*- coding:utf-8 -*-

{%- if cookiecutter.use_sql == 'yes' %}
#--- SQLALCHEMY SUPPORT

from extensions import db


class BaseModel(db.Model):
    __abstract__ = True
    __table_args__ = {'extend_existing': True}

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.iteritems():
            setattr(self, attr, value)

        return commit and self.save() or self

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()

        return self

    def delete(self, commit=True):
        db.session.delete(self)
        return commit and db.session.commit()

    @property
    def url(self):
        raise NotImplementedError('need to define url')


def drop_all():
    db.drop_all()


def create_all():
    db.create_all()


def remove_session():
    db.session.remove()

#--- SQLALCHEMY SUPPORT END
{% endif %}

{%- if cookiecutter.use_nosql == 'yes' %}
from extensions import nosql

{% endif %}
