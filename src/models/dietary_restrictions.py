class DietaryRestrictions:

    def __init__(self, id, restriction) -> None:
        self.id = id
        self.restriction = restriction

    def serialize(self):
        return {
            'id': self.id,
            'restriction': self.restriction
        }