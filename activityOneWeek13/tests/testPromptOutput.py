import json
from activityOneWeek13.app import extract_json_from_text

def test_extract_json_simple():
    text = 'Here is the plan:\n{"destination":"Kyoto","duration_days":3,"dates":{"start":"2025-12-01","end":"2025-12-03"},"budget":{"level":"Medium","estimate":"~800 JPY"},"interests":["food"],"itinerary":[],"packing_list":[],"travel_tips":""}'
    parsed = extract_json_from_text(text)
    assert parsed["destination"] == "Kyoto"
    assert parsed["duration_days"] == 3

def test_extract_json_malformed_commas():
    text = '{"destination":"X", "itinerary":[1,2,], }'
    parsed = extract_json_from_text(text)
    assert parsed is not None
