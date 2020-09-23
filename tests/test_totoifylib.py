import unittest
import json
from totoify_grafeas.totoifylib import (
    create_grafeas_occurrence_from_in_toto_link,
    create_in_toto_link_from_grafeas_occurrence,
    GrafeasInTotoTransport,
    GrafeasInTotoOccurrence,
    GrafeasLink)


class TestCreateInTotoLinkFromOccurrence(unittest.TestCase):
  def test_intoto_verify_link_from_occurence(self):
    """ Create link from occurrence and run in-toto verify """
    with open("occurrence_link.json", "r") as occ_f:
      occurrence_json = json.load(occ_f)
    with open("note_reduced.json", "r") as note_f:
      note_json = json.load(note_f)

    occ = create_in_toto_link_from_grafeas_occurrence(occurrence_json, "clone")
#    occ = GrafeasInTotoOccurrence(occurrence_json["intoto"],
#        note_json["intoto"]["step_name"],
#        occurrence_json["intoto"]["signed"]["products"][0]["resource_uri"])
#
#    link = create_in_toto_link_from_grafeas_occurrence(occ, note_json["intoto"]["step_name"])
    # run in-toto verify on this link - do I have to import intoto?


if __name__ == "__main__":
  unittest.main()
