from protorpc import messages
from protorpc import message_types

class User(messages.Message):

    name = messages.StringField(1)

class Tag(messages.Message):

    name = messages.StringField(1)


class TagCollection(messages.Message):

    items = messages.MessageField(Tag, 1, repeated = True)


class Butter(messages.Message):

    title = messages.StringField(1)

    content = messages.StringField(2)

    tags = messages.MessageField(TagCollection, 3)


class ButterCollection(messages.Message):

    items = messages.MessageField(Butter, 1, repeated = True)


