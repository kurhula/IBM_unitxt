import json

from unitxt.blocks import TaskCard
from unitxt.catalog import add_to_catalog
from unitxt.loaders import LoadFromDictionary
from unitxt.test_utils.card import test_card

with open("linked_schema.json") as f:
    data = json.load(f)

card = TaskCard(
    loader=LoadFromDictionary(data={"test": data}),
    task="tasks.schema_linking",
    templates="templates.schema_linking.all",
)

test_card(card, debug=False)

add_to_catalog(
    artifact=card,
    name="cards.schema_linking",
    overwrite=True,
)
