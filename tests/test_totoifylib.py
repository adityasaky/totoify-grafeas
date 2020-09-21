import unittest
import json
from totoify_grafeas.totoifylib import (
    create_grafeas_occurrence_from_in_toto_link,
    create_in_toto_link_from_grafeas_occurrence,
    GrafeasInTotoTransport,
    GrafeasInTotoOccurrence,
    GrafeasLink)


class TestCreateOccurrenceFromInTotoLink(unittest.TestCase):
  def test_intoto_verify_link_from_occurence(self):
    with open("occurrence_link.json", "r") as occ_f:
      occurence_json = json.load(occ_f)
    with open("note_reduced.json", "r") as note_f:
      note_json = json.load(note_f)
    
    
if __name__ == "__main__":
  unittest.main()
