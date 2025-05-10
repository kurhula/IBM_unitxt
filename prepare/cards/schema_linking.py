import json

from unitxt.blocks import Set, TaskCard
from unitxt.catalog import add_to_catalog
from unitxt.loaders import LoadFromDictionary

with open("linked_schema.json") as f:
    data = json.load(f)

card = TaskCard(
    loader=LoadFromDictionary(data={"test": data}),
    preprocess_steps=[
        Set(
            fields={
                "hint": "",
                "id": "",
            }
        ),
    ],
    task="tasks.schema_linking",
    templates="templates.schema_linking.all",
)

# test_card(card)

add_to_catalog(
    artifact=card,
    name="cards.schema_linking",
    overwrite=True,
)
